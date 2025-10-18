# QR Code Generator

A tiny, extremely simple QR code generator — one Python file, straightforward to use. Run the script, enter a URL or any text, and a QR image will be saved in the same directory.

## Quick start

1. Clone this repo:
```bash
git clone https://github.com/beast447/QR-code_generator.git
cd QR-code_generator
```

2. Run the script:
```bash
python3 qrapp.py
```

3. Follow the prompt: paste/type your URL or text and press Enter.

4. The QR code image will be saved to the same directory as the script.

## Example

Run:
```bash
python3 qrapp.py
```

Then enter:
```
https://example.com
```

You should see a message confirming that the QR image was created and saved (for example: `qr_2025-10-18_16-29-49.png` — actual filename depends on the script).

## Notes & Troubleshooting

- The script is intentionally minimal. If you see an error about a missing module, ensure you're running the script with Python 3 and that any required dependencies (if any) are installed.
- If the script prompts for a filename or saves with a timestamped name, check the current directory for the generated PNG.
- If the QR image is blank or unreadable, try a different text input or increase the terminal window width when copying/pasting long strings.

## Contributing

This project was created to be simple and educational. Contributions are welcome — open an issue or a pull request if you want to:
- add command-line flags (e.g., output filename or image size),
- bundle a requirements.txt,
- or improve error messages.

## License

Use as you like. If you want to add a specific license, feel free to open a PR to include it.
