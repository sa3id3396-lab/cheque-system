# Kuwait Bank Cheque Printing Software

A professional desktop application for managing and printing cheques for Kuwait banks with full Arabic language support, RTL support, and modern UI design.

## Features

✨ **Core Features:**
- ✅ Arabic language support (full RTL support)
- ✅ SQLite database for cheque history
- ✅ Add/Edit/Delete cheques
- ✅ Print cheques with accurate formatting
- ✅ PDF export functionality
- ✅ Professional and modern UI design
- ✅ Advanced search system
- ✅ Multiple bank selection
- ✅ Complete cheque history tracking
- ✅ Windows executable build (PyInstaller)

## Technology Stack

- **Framework:** PyQt6 - Modern GUI framework
- **Database:** SQLite3 - Lightweight, serverless database
- **PDF Generation:** ReportLab - Professional PDF creation
- **Language:** Python 3.9+
- **Build Tool:** PyInstaller - Create Windows executables

## Project Structure

```
cheque-system/
├── main.py                          # Application entry point
├── src/
│   ├── __init__.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── db_manager.py           # Database operations
│   │   └── models.py               # Data models
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── main_window.py          # Main application window
│   │   ├── dialogs/
│   │   │   ├── __init__.py
│   │   │   ├── cheque_dialog.py    # Add/Edit cheque dialog
│   │   │   ├── search_dialog.py    # Advanced search dialog
│   │   │   └── settings_dialog.py  # Application settings
│   │   └── widgets/
│   │       ├── __init__.py
│   │       ├── cheque_table.py     # Cheque history table
│   │       ├── bank_selector.py    # Bank selection widget
│   │       └── status_bar.py       # Custom status bar
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── pdf_generator.py        # PDF generation logic
│   │   ├── cheque_printer.py       # Print functionality
│   │   ├── arabic_utils.py         # Arabic language utilities
│   │   └── validators.py           # Input validation
│   ├── resources/
│   │   ├── banks_data.json         # Kuwait banks configuration
│   │   ├── fonts/
│   │   │   └── arabic_fonts.ttf    # Arabic font files
│   │   └── styles/
│   │       └── stylesheet.qss      # Application stylesheet
│   └── config/
│       ├── __init__.py
│       ├── settings.py             # Application settings
│       └── constants.py            # Global constants
├── tests/
│   ├── __init__.py
│   ├── test_database.py
│   ├── test_validators.py
│   └── test_pdf_generator.py
├── requirements.txt                 # Python dependencies
├── build.spec                       # PyInstaller build specification
└── build_executable.py              # Build script for Windows EXE
```

## Installation

### Prerequisites
- Python 3.9 or higher
- Windows 10 or later

### Setup

1. Clone the repository:
```bash
git clone https://github.com/sa3id3396-lab/cheque-system.git
cd cheque-system
```

2. Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

```bash
python main.py
```

### Building Windows Executable

```bash
python build_executable.py
```

This will create a standalone Windows executable in the `dist/` folder.

## Features Details

### Database Management
- Stores cheques with all details (amount, date, bank, payee)
- Maintains complete history with timestamps
- Export cheques data to CSV/JSON

### Arabic Support
- Full RTL (Right-to-Left) text layout
- Native Arabic number support
- Arabic bank names and validation
- Proper Arabic text rendering in PDFs

### Printing & PDF Export
- MICR (Magnetic Ink Character Recognition) number formatting
- Accurate cheque template positioning
- High-resolution PDF output
- Print preview before printing

### Security
- Data validation on all inputs
- Duplicate cheque detection
- Audit trail for all operations
- Encrypted database support (optional)

## Bank Configuration

The application supports all major Kuwait banks:
- National Bank of Kuwait (NBK)
- Gulf Bank
- Al Ahli Bank of Kuwait
- Commercial Bank of Kuwait
- Burgan Bank
- KAMCO Bank
- Boubyan Bank
- Warba Bank
- And more...

Banks data is stored in `src/resources/banks_data.json`

## Screenshots

[Screenshots will be added after first release]

## Keyboard Shortcuts

- `Ctrl+N` - New cheque
- `Ctrl+S` - Save cheque
- `Ctrl+P` - Print cheque
- `Ctrl+E` - Export to PDF
- `Ctrl+F` - Search cheques
- `Ctrl+D` - Delete cheque
- `F5` - Refresh data
- `F1` - Help & About

## Development

### Running Tests

```bash
pytest tests/
```

### Code Style

The project follows PEP 8 style guide. Run linting with:

```bash
flake8 src/
pylint src/
```

## Requirements

See `requirements.txt` for complete dependency list:
- PyQt6 - GUI framework
- PyQt6-sip - PyQt6 support
- reportlab - PDF generation
- sqlite3 - Database (included with Python)
- arabic-reshaper - Arabic text processing
- python-bidi - Bidirectional text support
- pytest - Testing framework
- pyinstaller - Create executables

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Support

For issues and feature requests, please visit: https://github.com/sa3id3396-lab/cheque-system/issues

## Author

Developed for Kuwait banking institutions.

## Version

Current Version: 1.0.0

---

**Last Updated:** 2026-05-26
