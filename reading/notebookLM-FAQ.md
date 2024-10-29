# Frequently Asked Questions

## **General Information** 

### **What are the available regions for NotebookLM?**

NotebookLM is available to all users (18+) in the[ 180+ regions where the Gemini API is available in](https://ai.google.dev/gemini-api/docs/available-regions).

### **Should I access NotebookLM on my desktop computer or my mobile device?**

While mobile is supported, at this time, NotebookLM is best viewed on a desktop computer.

### **How do I report offensive responses generated in NotebookLM?**

If you think a response generated in NotebookLM is offensive or unsafe, let us know by clicking on the *thumbs down* button and choose the *Offensive/unsafe* as the reason. We will review the report and take appropriate actions to improve the safety of our model.

### **How do I report a shared Notebook for infringing my rights?**

If you see content in a shared Notebook that you believe violates the law or your rights, let us know by clicking *Report Notebook*, which can be found in the three-dot menu for that Notebook on the homepage or via this[ direct link](https://docs.google.com/forms/d/e/1FAIpQLScuBnjHhHhB4BzQ7nvr2qEybg3hL4cav5p1Orwn2meVS8e-tQ/viewform?resourcekey=0-BVvxGxRQsb95yMfYuQD30w). We will review the material and consider blocking, limiting, or removing access to it.

### **What about the privacy of my data in NotebookLM?**

NotebookLM will never train on any of your data. Please read more [here](https://support.google.com/notebooklm/answer/14275965?hl=en&ref_topic=14775295&sjid=761901014805403279-NA). 

### **Which Gemini version does NotebookLM run on?**

As of July 2024, Gemini 1.5 Pro. We will continue to experiment on which model works best (and hopefully fastest) to serve our users so this may change over time

 

## **Features and Capabilities**

### **Will updates to the Google Doc or Slides be reflected in NotebookLM?**

When you import a Google Doc or Slides into NotebookLM, we make a copy of the original Google Doc in NotebookLM at the moment of upload. Past this point, the app doesn’t keep track of changes to the file automatically, including access to it. NotebookLM can’t delete or edit your original files. You have to manually re-upload any local file, or use the *Click to Sync with Drive* button to refresh imported Google Docs and Slides in the source viewer.

### **What is the maximum file size limit for sources in NotebookLM?**

The current limit is 500,000 words per source. There is no page limit.

### **What languages does NotebookLM support?**

NotebookLM currently supports over 35 languages. You can change your language preference in your Google Account [settings](https://myaccount.google.com/language?pli=1).

### **Does NotebookLM support PDFs?**

Yes, NotebookLM supports PDFs. However, there are some limitations:

- **Image only PDF:** Starting September 2024, image-only PDFs will be better supported. While NotebookLM is improving its handling of images in PDFs, you may need to re-upload previously imported PDFs as functionality improves.

### **Do you have any tips on how I should get NotebookLM to summarize a source?**

NotebookLM offers two modes for summarizing sources: you may ask for a summary of specific topics from your source directly in the chat, or you can find an auto-generated summary of the entire source in the *Source Guide* by clicking to open a source in the left hand side source viewer.

When you ask for summaries in the chat for more specific summaries, try these tips:

- Ask specific questions about the information you're looking for. If you have multiple sources selected, try including source names in your query to help NotebookLM narrow down the search. For example, instead of "Summarize this source," try "Summarize key findings about dog training from the source document titled Dog Training 101."

### **Can I work on a note collaboratively with others in real-time?**

Yes! Note edits are reflected in real-time for all collaborators. If you have the same notebook open, any changes made by one person will appear for everyone else who has the notebook open. Only users being added as an “editor” to a shared Notebook can edit notes.

### **Why does NotebookLM sometimes say it can’t answer my question?**

There are a few reasons why NotebookLM might not be able to answer your question:

- **Safety Flags:** The content of your source might contain language that triggers a safety flag. This can occur with sensitive topics like violence, sexuality, or obscenity, even in historical contexts.
- **Unclear Phrasing:** Try rephrasing your question to be clearer or more specific. When your notebook contains a large set of sources (that exceeds the LLM’s context window size), NotebookLM needs to first retrieve the most relevant information based on your question then try to build a response using this information. A more specific question will help NotebookLM locate these relevant bits of information.
- **Information Not in Sources:** NotebookLM is designed to answer questions based on the information provided in your uploaded sources. If the answer isn't in the source material, it won't be able to provide a response.

### **When I import a source via URL, how does NotebookLM handle HTML sources with interactive elements?**

Only the visible text on the page is imported. Improvements to this import type are underway.

### **How are sources, chat context, and notes used in responding to prompts?**

- **Notes:** Only used when specifically selected
- **Sources:** Always used, either the entire set or the subset you've selected.
- **Conversation History:** Also utilized in generating responses.

### **Is there a dark theme?**

Yes, you can switch between light/dark/auto mode using the sun icon in the top right corner.

 

## **Troubleshooting**

### **My source import failed, why?**

If the source length exceeds the allowed word limit (500,000 words per source), or if your original PDF file is copy-protected, NotebookLM won't be able to import those sources.

### **Why can't I access NotebookLM on my company or edu email address?**

NotebookLM is currently available to personal Google accounts and participating enterprise Google Workspace or Google Workspace for Education users.

If you are using a company or edu email address and unable to access the app, please review [this help center article](https://support.google.com/a/answer/13515709) and work with your workspace Admin to enable the NotebookLM app for your organization.

### **Why does my document look different in NotebookLM?**

When you upload a document, NotebookLM may reformat the content in order to to parse the content.

### **Why don’t I always get citations?** 

If your source content is too short, NotebookLM will reference the entire document without citing individual text from your source.

### **Why do different suggested actions show up?**

Different suggested actions are displayed based on what you have selected. For example, the *Combined notes* action is only applicable when you’ve selected multiple notes, and the *Summarize to note* action is only relevant when you highlight a block of text in a source document.

### **I can't access NotebookLM. What could be the reason?**

Common reasons include:

- Your country may not be supported (https://ai.google.dev/gemini-api/docs/available-regions).
- You might be using a school or work-managed account (e.g. x@y.edu), and your organization’s admin needs to enable access to the NotebookLM app.
- Only 18+ users are permitted to use the app.

### **Why am I getting the message "Access to Google Drive data has been disabled for this account"?**

This should only happen if you are using a school or work-managed account.

Check with your organization’s admin to see if the Core data access toggle is enabled for your organization: https://support.google.com/a/answer/13515709. 

## **Known Limitations** 

### **Does chat history persist between sessions?**

This is currently not supported. There is no capability to save the chat between sessions or screen refreshes. You can save notes by pinning the response. 

### **Is there a way to recover deleted notes in NotebookLM?**

Unfortunately, there's no way to recover deleted notes at this time.

### **Does NotebookLM import footnotes from Google Docs?**

Not yet, but the team is aware of this.

### **Is there a NotebookLM app?**

There's no dedicated app for now, but you might be able to install a website shortcut as a progressive web app in some browsers. 

### **Can I make a saved note a source? Can I duplicate a notebook?**

Neither action is directly supported for now. You can always copy and paste the content in a note and add that as a new source.

### **Can I customize study guides, for example, into Anki cards for medical school?**

Not at this moment but it's on our radar.

### **Will user customizations, like preferred explanation styles, be supported and saved across sessions?**

Not currently, but a feature to preserve these preferences is being explored.