import requests
import time
import json


CROSSREF_CACHE = {}


# ==========================================
# CROSSREF VENUE FALLBACK
# ==========================================
def crossref_venue(doi, contact_email):

    if not doi:
        return None

    doi = doi.replace("https://doi.org/", "")

    if doi in CROSSREF_CACHE:
        return CROSSREF_CACHE[doi]

    try:

        response = requests.get(
            f"https://api.crossref.org/works/{doi}",
            timeout=5,
            headers={"User-Agent": f"mailto:{contact_email}"},
        )

        if response.status_code != 200:
            CROSSREF_CACHE[doi] = None
            return None

        data = response.json().get("message", {})

        # Journal / proceedings
        container = data.get("container-title")

        if container:

            CROSSREF_CACHE[doi] = container[0]
            return container[0]

        # Conference fallback
        event = data.get("event")

        if event:

            venue = event.get("name")

            CROSSREF_CACHE[doi] = venue
            return venue

    except Exception:

        pass

    CROSSREF_CACHE[doi] = None

    return None


# ==========================================
# VENUE EXTRACTION
# ==========================================
def extract_venue(work, contact_email):

    # 1. OpenAlex primary location
    primary_location = work.get("primary_location") or {}

    source = primary_location.get("source")

    if source and source.get("display_name"):

        return source["display_name"]

    # 2. OpenAlex locations fallback
    for location in work.get("locations") or []:

        source = location.get("source")

        if source and source.get("display_name"):

            return source["display_name"]

    # 3. OpenAlex best OA location
    best_oa = work.get("best_oa_location") or {}

    source = best_oa.get("source")

    if source and source.get("display_name"):

        return source["display_name"]

    # 4. Crossref DOI lookup
    venue = crossref_venue(work.get("doi"), contact_email)

    if venue:

        return venue

    # 5. Preprint fallback
    if work.get("type") == "preprint":

        return "arXiv"

    return "Unknown Venue"


# ==========================================
# TITLE NORMALIZATION
# ==========================================
def normalize_title(title):

    if not title:
        return ""

    return (
        title.lower()
        .replace(":", "")
        .replace(",", "")
        .replace(".", "")
        .replace("-", " ")
        .replace("_", " ")
        .strip()
    )


# ==========================================
# AUTHOR LOOKUP
# ==========================================
def find_author(name, headers):

    response = requests.get(
        "https://api.openalex.org/authors",
        headers=headers,
        params={
            "search": name,
            "per-page": 10,
        },
    )

    response.raise_for_status()

    results = response.json().get("results", [])

    if not results:
        return None

    # Prefer University of Innsbruck authors
    for author in results:

        institutions = author.get("last_known_institutions") or []

        for institution in institutions:

            if "innsbruck" in institution.get("display_name", "").lower():

                return author

    return results[0]


# ==========================================
# FETCH PAPERS
# ==========================================
def fetch_raw_papers(author_config, contact_email):

    headers = {"User-Agent": f"mailto:{contact_email}"}

    all_raw_papers = []

    for name, years in author_config.items():

        start_year, end_year = years

        print(f"Fetching data for: {name} " f"({start_year}-{end_year})...")

        try:

            author = find_author(name, headers)

            if not author:

                print("  -> Could not find OpenAlex author")

                continue

            author_id = author["id"].split("/")[-1]

            page = 1

            while True:

                response = requests.get(
                    "https://api.openalex.org/works",
                    headers=headers,
                    params={
                        "filter": (
                            f"author.id:{author_id},"
                            f"from_publication_date:"
                            f"{start_year}-01-01,"
                            f"to_publication_date:"
                            f"{end_year}-12-31"
                        ),
                        "per-page": 200,
                        "page": page,
                    },
                )

                response.raise_for_status()

                works = response.json().get("results", [])

                if not works:
                    break

                for work in works:

                    if not work.get("title"):

                        continue

                    full_author_list = []

                    for authorship in work.get("authorships") or []:

                        author_data = authorship.get("author") or {}

                        if author_data.get("display_name"):

                            full_author_list.append(author_data["display_name"])

                    all_raw_papers.append(
                        {
                            "title": work["title"],
                            "year": work.get("publication_year"),
                            "citations": work.get("cited_by_count", 0),
                            "link": (work.get("doi") or work.get("id")),
                            "venue": extract_venue(work, contact_email),
                            "open_access": (
                                work.get("open_access", {}).get("is_oa", False)
                            ),
                            "all_authors": full_author_list,
                            "queried_group_member": name,
                        }
                    )

                page += 1

                time.sleep(0.1)

        except Exception as e:

            print(f"  -> Error fetching {name}: {e}")

    return all_raw_papers


# ==========================================
# DEDUPLICATION
# ==========================================
def remove_duplicates(raw_papers_list):

    print(f"\nProcessing {len(raw_papers_list)} " "raw papers for duplicates...")

    unique_papers = {}

    for paper in raw_papers_list:

        keys = []

        if paper.get("link"):

            keys.append("link:" + paper["link"].lower())

        title_key = normalize_title(paper.get("title"))

        if title_key:

            keys.append("title:" + title_key)

        existing = None

        for key in keys:

            if key in unique_papers:

                existing = unique_papers[key]
                break

        if existing is None:

            clean_paper = paper.copy()

            clean_paper["group_authors"] = [clean_paper.pop("queried_group_member")]

            for key in keys:

                unique_papers[key] = clean_paper

        else:

            member = paper["queried_group_member"]

            if member not in (existing["group_authors"]):

                existing["group_authors"].append(member)

    final_list = []

    seen = set()

    for paper in unique_papers.values():

        if id(paper) not in seen:

            seen.add(id(paper))

            final_list.append(paper)

    final_list.sort(
        key=lambda x: (x.get("year", 0), x.get("citations", 0)),
        reverse=True,
    )

    return final_list


# ==========================================
# EXECUTION
# ==========================================
if __name__ == "__main__":

    # Author -> (start year, end year)
    research_group = {
        "Thomas Fahringer": (2020, 2026),
        "Peter Thoman": (2020, 2026),
        "Philipp Gschwandtner": (2020, 2026),
        "Stefan Pedratscher": (2020, 2026),
        "Juan Aznar-Poveda": (2022, 2026),
        "Marlon Etheredge": (2022, 2026),
        "Zahra Najafabadi-Samani": (2023, 2026),
        "Siavash Razmi": (2025, 2026),
        "Aryan Pathare": (2026, 2026),
        "Gabriel Mitterrutzner": (2025, 2026),
        "Philip Salzmann": (2022, 2025),
    }

    my_email = "your.email@uibk.ac.at"

    raw_data = fetch_raw_papers(research_group, my_email)

    clean_data = remove_duplicates(raw_data)

    duplicates_removed = len(raw_data) - len(clean_data)

    print(f"\nFinished! Removed " f"{duplicates_removed} duplicates.")

    if clean_data:

        sample = clean_data[0]

        print("\n--- Example Output ---")

        print(f"Title: {sample['title']}")

        print(f"Venue: {sample['venue']}")

        print("Group Authors: " + ", ".join(sample["group_authors"]))

        print("----------------------\n")

    filename = "_data/publications.json"

    with open(filename, "w", encoding="utf-8") as f:

        json.dump(clean_data, f, indent=4, ensure_ascii=False)

    print(f"✅ Success! Data saved to {filename}")
