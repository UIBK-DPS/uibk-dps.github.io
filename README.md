# DPS Website Contribution Guide

This document explains how to update the DPS website content, including team profiles, research projects, and bachelor/master thesis topics.

The website is automatically generated from Markdown files. After adding, editing, or removing Markdown files and pushing the changes, the website will be updated automatically.

## General Guidelines

- Only modify the **content values** inside the Markdown files.
- Do **not** change the file structure, metadata field names, or YAML format.
- The website automatically detects new, modified, or removed Markdown files.
- The recommended workflow is to copy an existing file, modify the content, and commit the changes.

---

## Quickstart

| Task                        | Location                                   |
| --------------------------- | ------------------------------------------ |
| Update your profile         | `_team/`                                   |
| Change your profile picture | `images/team/`                             |
| Add a thesis topic          | `_thesis/`                                 |
| Remove a thesis topic       | Delete the Markdown file from `_thesis/`   |
| Add a project               | `_projects/`                               |
| Remove a project            | Delete the Markdown file from `_projects/` |

---

## Submitting Changes Through a Pull Request

All modifications to the DPS website should be submitted through a GitHub Pull Request (PR). Contributors should create a fork of the DPS website repository, apply their changes in their own fork, and submit a PR to the main repository. This allows changes to be reviewed before they are merged into the main branch and published on the website.

Before creating a Pull Request, make sure that your changes are limited to the required content files and that the Markdown format has been preserved. Once the Pull Request is approved and merged, the website deployment pipeline will automatically rebuild the website and publish the updated content.

1. Fork the DPS website repository on GitHub.
2. Clone your fork locally: `git clone https://github.com/<your-username>/uibk-dps.github.io.git`
3. Create a new branch for your changes: `git checkout -b update-website-content`
4. Modify the required files.
5. Review your changes: `git status`
6. Add the modified files: `git add .`
7. Commit your changes using [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
8. Push your branch to your fork: `git push origin update-website-content`
9. Open a Pull Request from your fork to the DPS website repository.

Your PR will be reviewed and merged as soon as possible by the DPS website admin team.

## 1. Updating Team Profiles

Team member profile are located in: `_team/` folder.

Each team member has a dedicated Markdown file.

To update your profile:

1. Open your Markdown file.
2. Modify only the content.
3. Keep the existing structure and metadata fields unchanged.

> **Allowed Job Titles / Positions:** "Postdoctoral Univ. Assistant", "Ph.D. student", "Research assistant", "Full Professor", "Associate Professor"

Example:

```markdown
---
title: "Dr. Max Mustermann"
date: 2018-11-19T10:47:58+10:00
jobtitle: "Postdoctoral Univ. Assistant"
linkedinurl: "https://www.linkedin.com/"
scholarurl: "https://scholar.google.com/"
orcidurl: "https://orcid.org/0000-0000-0000-0000"
weight: 2
admin: false
image: "images/team/max.jpg"
room: "3M04"
office_hours: "To be arranged"
email: "max.mustermann@uibk.ac.at"
phone: "+43 512 507 00000"
---

Max received his Ph.D. degree in Computer Science from the University of Innsbruck, Austria, in 2022. He was awarded the prize “Example Prize” (national level) for the best B.Sc. thesis in 2016. He is currently a postdoctoral researcher at the Distributed and Parallel Systems group of the University of Innsbruck, Austria. His research interests include Distributed Systems, Distributed Storages, Distributed Machine learning, Cyber-Physical Systems (CPS), Internet of Things, and Wireless networks and communications.
```

Profile pictures are located in: `images/team/` folder.

To update your picture:

1. Replace your existing image with the new one.
2. Keep the expected filename and format.
3. Use an appropriate professional picture in grayscale.

## 2. Adding or Updating Bachelor/Master Thesis Topics

Thesis topics are located in: `_thesis/` folder.

To add a new thesis topic:

1. Create a new Markdown file.
2. Use the following naming convention: `name_keyword1_keyword2.md`

Example:

```juan_distributed_stream_processing.md```

Add the required metadata fields.
Modify only the values.

Example:

```
---
title: "Scalable and Adaptive Stream Processing Architectures"
supervisor: "Thomas Fahringer"
weight: 1
desired_skills: "Distributed Systems, Stream Processing, Cloud Deployment"
master: true
short: "Designing and evaluating adaptive algorithms and architectures for high-throughput, low-latency real-time data processing."
number_of_students: "1–2 (preferred)"
language: "English"
---
```

| Field                | Description                   | Example                                           |
| -------------------- | ----------------------------- | ------------------------------------------------- |
| `title`              | Thesis title                  | `"Adaptive Edge Computing Frameworks"`            |
| `supervisor`         | Thesis supervisor(s)          | `"Thomas Fahringer"`                              |
| `weight`             | Display order on the website  | `1`                                               |
| `desired_skills`     | Required background or skills | `"Distributed Systems, Kubernetes"`               |
| `master`             | Defines thesis type           | `true` = Master thesis, `false` = Bachelor thesis |
| `short`              | Short public description      | `"Designing scalable distributed systems"`        |
| `number_of_students` | Number of available students  | `"1–2"`                                           |
| `language`           | Thesis language               | `"English"`                                       |

To remove a thesis topic, simply delete the corresponding Markdown file.

## 3. Adding or Updating Research Projects

Research projects are located in: `_projects/` folder.

The procedure is the same as for thesis topics.
New projects will automatically appear on the website after deployment.

