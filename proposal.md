# Project Proposal

## 1. Project Identification
- **Project Title:** Discord Mood Ring Bot
- **Course:** CPT273 : Process Automation
- **Term:** Spring 2026
- **Student Name(s):** Abdullahi Mohamed, Makayla MacNeill, Jamie Cole
- **Primary Contact:** Jamie Cole
- **Proposed Start Date:** 04/10/26
- **Proposed End Date:** 05/03/26

---

## 2. Project Selection & Motivation
Describe why you selected this project and why you are a good fit.

Include:
- Personal or professional motivation
- Alignment with career goals
- Relevant interests or prior exposure

    We chose this project because Makayla mentioned it in passing in our discord group. The server mood seems like a fun thing to track, as well as it being attuned to our interests in the technology field. It includes elements both computer science and working with people, as we will need to make the bot able to respond to requests from the users. 

---

## 3. Problem Statement
Clearly describe the problem, need, or opportunity this project addresses.

Answer:
- What problem exists?
- Who is affected?
- Why does this problem matter?

Limit to 1–2 focused paragraphs.

    There isn't necessarily a problem here, but tracking the server mood will allow us to see how the mood spikes given the discussion topics. For example, if it's some kind of psuedo-political topic, such as AI usage in the healthcare industry, then the mood might differ greatly for the week than if there isn't a general discussion. 

---

## 4. Proposed Solution Overview
Provide a high-level description of your proposed solution.

Include:
- What you intend to build, deploy, or configure
- Core features or capabilities
- Explicit exclusions (what the project will *not* include)

    The idea is that there will be a discord bot that tracks the mood of the server. It will give updates on the mood of the server daily, and be able to respond to queries from the students who, for example, ping it with a command. It could present the top mood of the hour, day, week, and perhaps month.

---

## 5. Technical Stack & Tools
List the technologies you expect to use.  Please note that this solution MUST live within the cpt.internal network and must be maintainable by future students.

- **Operating System(s):** Linux, so that it can opperate on a schedule
- **Programming Language(s):** Python
- **Frameworks / Libraries:** Discord Library, Requests, A library that assigns mood to text (NRCLex)
- **Databases / Storage:** N/A
- **Infrastructure (VMs, containers, etc.):** Guacamole VMs
- **Tools (Git, CI, monitoring, APIs, etc.):** GIT, APIs, Discord

---

## 6. Prerequisite Knowledge & Skills
Assess your readiness for this project.

Include:
- Skills you already have
- Skills you need to learn
- Relevant coursework completed
- Prior projects or experience

Be honest—this section helps scope the project appropriately.

    All three of us have experience working with API's, and data formatting, as we are in the final stretch of Process Automation. We also have experience with CRON job scheduling, for the same reason. 

    We will likely need to learn how to operate a discord bot that takes requests from users, and working with a new library that gives moods to text.

---

## 7. Project Scope & Deliverables
Define what success looks like.

Include:
- Minimum viable deliverable (MVP)
- Required outputs (application, scripts, documentation, etc.)
- Optional stretch goals (if time permits)

    Our minimum viable deliverable will be the discord bot that uploads the mood on a scheduled basis, and responds to users requests to ping it. Our required outputs will need to be the application and every script that goes with it. 

---

## 8. Milestones & Timeline
Provide a rough timeline broken into phases.

Example:
- Phase 1: Research & Design
- Phase 2: Core Implementation
- Phase 3: Testing & Refinement
- Phase 4: Documentation & Presentation

Dates do not need to be exact, but planning is required.

    Phase 1: Researching and Job delagating
    Phase 2: Working on code
    Phase 3: Discord implimentation
    Phase 4: Presentation
---

## 9. Risks, Constraints & Dependencies
Identify potential challenges.

Include:
- Technical risks
- Time constraints
- External dependencies (APIs, credentials, access)
- Mitigation strategies

    Our techincal risks are simply that we may not be able to do it without going against discords policies. We've seen some stuff that states that you shouldn't pull text data using the API, but we've also seen conflicting information regarding it with the discord python library. We should have a back up plan just in case we aren't legally allowed to do it. 

---

## 10. Security, Ethics & Safety Considerations
Address any relevant concerns, such as:
- Authentication and authorization
- Data sensitivity
- Network exposure
- Logging, monitoring, or automation impact
- Ethical considerations

A brief assessment of all of these is required, even if it is "N/A".

    We would need to tokens for the discord server, and for every student/staff member on the server to know that their messages are indeed being pulled. 

---

## 11. Team Structure (If Applicable)
If working in a group, describe:
- Team roles
- Communication plan
- Conflict resolution approach
- Workload distribution

    Undecided
---

## 12. Documentation & Knowledge Transfer Plan
Explain how this project will be documented.  Please note that this should include documentation in the UVDesk knowledgebase at the very least.  Programming projects should include readme.md files. 

Include:
- README or user documentation
- Deployment or maintenance guides
- How another student or administrator could continue the project

    Github, with a README with instructions on how the discord bot works. 

---

## 13. Faculty/cpt.internal Resources Requested
List any required resources:
- VM access
- Network access
- Credentials or APIs
- Special permissions
- Hardware (if applicable)

Please be sure to consider any future tickets you may need to submit to complete this work as those will need to be generated and assigned to the appropriate groups as soon as feasibly possible once the project kicks off to ensure timely delivery.  I will step in to help where required but you will likely be working with students in other classes so please be cognizant of their time!

    We will simply need tokens for the discord server, and access to the CPT Guacamole vms. 

---

## 14. Acknowledgement of Expectations
By submitting this proposal, I acknowledge that:
- This is a self-directed technical project
- I am responsible for research and troubleshooting
- Evaluation will consider process, documentation, and professionalism

**Signature (Name & Date):**

Student 1:  __Jamie Aaron Cole__ Date: __04/08/26__
Student 2:  ___abdullahi mohamed_________________________ Date: _04/08/26______________
Student 3:  __Makayla MacNeill__ Date: __04/09/26_____
Student 4:  ____________________________ Date: _______________

Instructor: ____________________________ Date: _______________
