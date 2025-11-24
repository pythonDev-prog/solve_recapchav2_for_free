# ReCAPTCHA v2 Solver

An automated ReCAPTCHA v2 solver using Playwright and the NopeCHA browser extension. This tool helps bypass ReCAPTCHA challenges for testing and automation purposes.

## ⚠️ Disclaimer

This tool is intended for **educational and testing purposes only**. Use it responsibly and ethically:
- Only use on websites you own or have explicit permission to test
- Respect website terms of service and robots.txt
- Do not use for malicious purposes or unauthorized access
- Be aware of legal implications in your jurisdiction

## ✨ Features

- 🚀 Automated ReCAPTCHA v2 solving using NopeCHA extension
- 🎯 Command-line interface with customizable options
- 🛡️ Proper error handling and user feedback
- 📦 Easy to use with minimal configuration
- 🔧 Configurable timeout and wait times

## 📋 Prerequisites

- Python 3.7 or higher
- Playwright browser drivers
- NopeCHA browser extension

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/solve_recapchav2_for_free.git
   cd solve_recapchav2_for_free
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright browsers**
   ```bash
   playwright install chromium
   ```

4. **Get NopeCHA Extension**
   
   The NopeCHA extension is required for this tool to work. You have two options:
   
   **Option A: Use included extension (if available)**
   - The extension should already be in the `extension/nopecha-extensionC` folder
   
   **Option B: Download manually**
   - Visit [NopeCHA website](https://nopecha.com/) or Chrome Web Store
   - Download the extension
   - Extract it to `extension/nopecha-extensionC` folder

## 💻 Usage

### Basic Usage

Run the script with default settings (Google ReCAPTCHA demo):
```bash
python solve_recaptchav2.py
```

### Custom URL

Solve ReCAPTCHA on a specific URL:
```bash
python solve_recaptchav2.py --url "https://example.com/form"
```

### Custom Wait Time

Specify how long to wait (in seconds):
```bash
python solve_recaptchav2.py --wait-time 300
```

### Headless Mode

Run browser in headless mode (not recommended for ReCAPTCHA):
```bash
python solve_recaptchav2.py --headless
```

### All Options

```bash
python solve_recaptchav2.py --url "https://example.com" --wait-time 300 --timeout 60000
```

## 🔧 Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--url` | URL to visit | Google ReCAPTCHA demo |
| `--wait-time` | Time to wait in seconds | 360 (6 minutes) |
| `--headless` | Run browser in headless mode | False |
| `--timeout` | Page navigation timeout (ms) | 90000 |

## 📖 How It Works

1. The script launches a Chromium browser with the NopeCHA extension loaded
2. It navigates to the specified URL
3. The NopeCHA extension automatically detects and solves ReCAPTCHA v2 challenges
4. The script waits for the specified duration to allow solving to complete
5. Browser closes automatically after the wait time

## 🐛 Troubleshooting

### Extension Not Found Error
```
FileNotFoundError: Extension directory not found
```
**Solution**: Ensure the NopeCHA extension is in `extension/nopecha-extensionC` folder.

### Playwright Not Installed
```
Error: Playwright browser not found
```
**Solution**: Run `playwright install chromium`

### ReCAPTCHA Not Solving
- Make sure the NopeCHA extension is properly configured
- Try increasing the `--wait-time` parameter
- Check that you're using the correct extension version
- Avoid using `--headless` mode as it may interfere with solving

### Page Load Timeout
```
Playwright error: Timeout exceeded
```
**Solution**: Increase timeout using `--timeout 120000` (2 minutes)

## 📁 Project Structure

```
solve_recapchav2_for_free/
├── solve_recaptchav2.py    # Main script
├── requirements.txt         # Python dependencies
├── README.md               # This file
├── LICENSE                 # MIT License
├── .gitignore             # Git ignore rules
└── extension/             # Browser extension folder
    └── nopecha-extensionC/  # NopeCHA extension
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Playwright](https://playwright.dev/) - Browser automation framework
- [NopeCHA](https://nopecha.com/) - ReCAPTCHA solving extension
- Built for educational and testing purposes

## ⚖️ Legal Notice

This software is provided "as is" without warranty of any kind. The authors are not responsible for any misuse or damage caused by this program. Always ensure you have proper authorization before testing any website.

---

**Made with ❤️ for ethical testing and automation**
