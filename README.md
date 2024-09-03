# $HitCoin

$HitCoin is a fun-themed Telegram mini-app that allows users to mine $HitCoin on the TON network by completing daily tasks.

## Features

- **Mining**: Users can mine $HitCoin by completing daily tasks.
- **Daily Tasks**: Daily tasks are listed for users to complete.
- **Shit Theme**: The app is designed with a playful "shit" theme.

## Directory Structure

```
HitCoin/
├── bot/
│   ├── main.py
├── contract/
│   ├── hitcoin.func
│   ├── hitcoin.abi.json
├── ui/
│   ├── index.html
│   ├── style.css
│   └── script.js
└── README.md
```

## How to Run

1. Set up a virtual environment and install the required dependencies:

   ```sh
   pip install aiogram ton-sdk-python
   ```

2. Deploy the smart contract using TON CLI.

3. Run the Telegram bot:

   ```sh
   python bot/main.py
   ```

## License

This project is licensed under the MIT License.
