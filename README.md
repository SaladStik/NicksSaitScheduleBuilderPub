# Nick's SAIT Schedule Builder 🎓

Built by [Nicholas Irvine (SaladStik)](https://github.com/SaladStik)

A powerful web app that helps SAIT students explore **ALL** possible schedule combinations and automatically generate personalized timetables. Browse through hundreds of valid schedules, find the perfect one, and export it directly to your calendar!

## 🚀 Quick Start

1. **Clone the repository:**

```bash
git clone https://github.com/SaladStik/NicksSaitScheduleBuilder
cd Class-Schedule-Management
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the app:**

```bash
streamlit run streamlit_app_advanced.py
```

4. **Open in your browser:**
   The app will automatically open at `http://localhost:8501`

That's it! No database setup, no configuration files needed. Just run and go! 🎉

---

## ✨ What Can This App Do?

### 🔍 **Smart Course Search**

- Search for any SAIT course with autocomplete
- Real-time integration with SAIT Banner system
- See live seat availability
- Filter by available seats or view all sections (including full ones)
- Auto-import sections directly to your schedule

### 📚 **Class Registration**

- **Search & Add:** Find courses from Banner and add them instantly
- **Manual Entry:** Add custom classes with full schedule control
- **API Import:** Bulk fetch all your program's courses at once
- **File Import:** Load class data from saved JSON files

### ⏱️ **Intelligent Schedule Creator**

- Generate **ALL** possible schedule combinations automatically
- Browse through hundreds of valid schedules
- Set mandatory classes you must take
- Mark preferred free days
- View conflict-free schedules ranked by your preferences
- Beautiful visual timetable with color-coded classes
- **Switch colors** button to randomize schedule colors

### 🗑️ **Drop Classes Tab**

- View your currently registered classes from Banner
- Drop classes directly through the app
- See instructor, CRN, and seat availability
- One-click access to refresh your registration

### 📅 **Calendar Export**

- Auto-fetches your registered schedule from Banner
- Set custom semester start/end dates
- Download as ICS file for any calendar app
- Includes instructor names and room locations
- Import to Google Calendar, Outlook, Apple Calendar, etc.

### 🚀 **Apply Schedule to Banner** _(Experimental)_

- Automatically register for your chosen schedule
- Adds classes to registration cart and submits
- Tracks registration status and failures
- Handles full classes and time conflicts

---

## 🏗️ Architecture

This app is **completely stateless** and privacy-focused:

- ✅ **No database required** - runs entirely in your browser
- ✅ **No server storage** - all data in browser session state
- ✅ **Privacy first** - your Banner credentials never leave your session
- ⚠️ **Session-based** - data is lost when you refresh/close tab
- � **Download to save** - export schedules to Excel or ICS to keep them

---

## 🔐 Banner API Authentication

The app integrates with SAIT's Banner system for live data. You'll be guided through authentication on first use:

1. Open SAIT Banner in your browser
2. Use Chrome DevTools (F12) to capture request headers
3. Paste into the app - takes 30 seconds
4. _(Optional)_ Skip authentication and use manual entry instead

Your tokens are stored **only in your browser session** and are **never sent to any server**.

---

## � Compatibility Notes

- **Desktop:** Fully tested on Chrome, Edge, Firefox
- **Mobile:** May have limited functionality - desktop/laptop recommended
- **Technical users:** Built with technical users in mind, but designed to be accessible to everyone

---

## 🤝 Connect

- 💼 [LinkedIn - Nicholas Irvine](https://www.linkedin.com/in/nicholas-irvine-303ab5284/)
- 🐙 [GitHub - @SaladStik](https://github.com/SaladStik)

---

## 📝 License

This project is open source. Feel free to fork, modify, and use for your own schedule building needs!

---

## 🙏 Credits

This is an **extremely modified version** of the original [Class-Schedule-Management](https://github.com/nicocanta20/Class-Schedule-Management) by nicocanta20. The codebase has been significantly enhanced with SAIT-specific integrations, UI improvements, and new features.

---

**Made with ❤️ for SAIT students by a SAIT student**
