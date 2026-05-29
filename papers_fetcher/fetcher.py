import requests
import time
import json


# ==========================================
# 1. FETCHING LOGIC
# ==========================================
def fetch_raw_papers(author_names, target_years, contact_email):
    headers = {"User-Agent": f"mailto:{contact_email}"}
    all_raw_papers = []

    years_str = "|".join(map(str, target_years))

    for name in author_names:
        print(f"Fetching data for: {name}...")

        author_url = f"https://api.openalex.org/authors?search={name}"
        try:
            author_response = requests.get(author_url, headers=headers)
            author_response.raise_for_status()
            author_data = author_response.json()

            if not author_data.get("results"):
                print(f"  -> Could not find an OpenAlex profile for {name}.")
                continue

            author_id = author_data["results"][0]["id"].split('/')[-1]

            works_url = (f"https://api.openalex.org/works?"
                         f"filter=author.id:{author_id},publication_year:{years_str}"
                         f"&per-page=200")

            works_response = requests.get(works_url, headers=headers)
            works_response.raise_for_status()
            works_data = works_response.json()

            for work in works_data.get("results", []):
                if not work.get("title"):
                    continue

                # --- NEW: Extract the full list of authors ---
                full_author_list = []
                for authorship in work.get("authorships", []):
                    author_data = authorship.get("author", {})
                    if author_data and author_data.get("display_name"):
                        full_author_list.append(author_data["display_name"])
                # ---------------------------------------------

                journal_name = "Unknown Venue"
                if work.get("primary_location") and work["primary_location"].get("source"):
                    journal_name = work["primary_location"]["source"].get("display_name", "Unknown Venue")

                all_raw_papers.append({
                    "title": work["title"],
                    "year": work["publication_year"],
                    "citations": work["cited_by_count"],
                    "link": work.get("doi") or work.get("id"),
                    "venue": journal_name,
                    "open_access": work.get("open_access", {}).get("is_oa", False),
                    "all_authors": full_author_list,  # Saves the complete author list
                    "queried_group_member": name  # Tracks which of YOUR group members found it
                })

            time.sleep(0.1)

        except Exception as e:
            print(f"  -> Error fetching {name}: {e}")

    return all_raw_papers


# ==========================================
# 2. DEDUPLICATION LOGIC
# ==========================================
def remove_duplicates(raw_papers_list):
    print(f"\nProcessing {len(raw_papers_list)} raw papers for duplicates...")

    unique_papers_dict = {}

    for paper in raw_papers_list:
        unique_id = paper.get("link") or paper.get("title", "").lower()

        if unique_id not in unique_papers_dict:
            clean_paper = paper.copy()
            # Convert the single queried member into a list of group authors
            clean_paper["group_authors"] = [clean_paper.pop("queried_group_member")]
            unique_papers_dict[unique_id] = clean_paper
        else:
            # If it's a duplicate, just add the group member to the group_authors list
            group_member = paper["queried_group_member"]
            if group_member not in unique_papers_dict[unique_id]["group_authors"]:
                unique_papers_dict[unique_id]["group_authors"].append(group_member)

    final_list = list(unique_papers_dict.values())
    final_list.sort(key=lambda x: (x.get("year", 0), x.get("citations", 0)), reverse=True)

    return final_list


# ==========================================
# 🚀 EXECUTION
# ==========================================
if __name__ == "__main__":

    research_group = [
        "Thomas Fahringer", "Peter Thoman", "Philipp Gschwandtner",
        "Stefan Pedratscher", "Juan Aznar-Poveda", "Marlon Etheredge",
        "Zahra Najafabadi-Samani", "Siavash Razmi", "Aryan Pathare",
        "Gabriel Mitterrutzner", "Philip Salzmann"
    ]

    TARGET_YEARS = [2022, 2023, 2024, 2025, 2026]
    my_email = "your.email@uibk.ac.at"

    raw_data = fetch_raw_papers(research_group, TARGET_YEARS, my_email)
    clean_data = remove_duplicates(raw_data)

    duplicates_removed = len(raw_data) - len(clean_data)
    print(f"\nFinished! Removed {duplicates_removed} duplicate(s).")

    # Let's print out the first paper to see the new author list in action
    if clean_data:
        print("\n--- Example Output ---")
        sample = clean_data[0]
        print(f"Title: {sample['title']}")
        print(f"Group Authors (Your team): {', '.join(sample['group_authors'])}")

        # Displaying the first 5 authors from the full list, just for the terminal preview
        full_authors_str = ", ".join(sample['all_authors'][:5])
        if len(sample['all_authors']) > 5:
            full_authors_str += " et al."
        print(f"All Authors: {full_authors_str}")
        print("----------------------\n")

    min_yr, max_yr = min(TARGET_YEARS), max(TARGET_YEARS)
    filename = f"../_data/publications.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(clean_data, f, indent=4)

    print(f"✅ Success! Data saved to {filename}")