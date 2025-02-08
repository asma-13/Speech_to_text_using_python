# 🎙️ Speech to Text Using Python

This is a **Speech-to-Text** project using **Python** and the `speech_recognition` library. It converts spoken words into text using the Google Speech Recognition API.

---

## 📌 Features

- ✅ **Real-time speech recognition** using a microphone
- ✅ **Handles ambient noise** for better accuracy
- ✅ **Error handling** for unrecognized speech and connection issues
- ✅ **Uses Google Speech Recognition API**

---

## 🖥️ Technologies Used

- **Python**
- **SpeechRecognition Library**
- **Google Speech-to-Text API**
- **Microphone Input Handling**

---

## 📜 How to Run the Program?

### 1️⃣ Install Required Libraries
Ensure you have Python installed, then run:
```bash
pip install speechrecognition pyaudio
```
If you face issues installing `pyaudio`, use:
```bash
pip install pipwin
pipwin install pyaudio
```

### 2️⃣ Run the Python Script
```bash
python speech_to_text.py
```

---

## 📝 How It Works

1. The script **initializes the microphone** and listens for speech.
2. It **adjusts for ambient noise** before capturing audio.
3. The **Google Speech Recognition API** processes the recorded speech.
4. The converted text is displayed in the terminal.
5. Handles errors if speech is unclear or there is an API request issue.

---

## 🎤 Example Output

```
-------------------------------------------------------------
|                         SPEECH TO TEXT                    |
|                            MADE BY                        |
|            ASMA CHANNA, MUHAMMAD USMAN, SOYAM KAPOOR                                   |
-------------------------------------------------------------
Please say something using your microphone:
Hello, how are you?

Recognized Text: Hello, how are you?
```

---

## 🛠️ Future Enhancements

- 📌 **Support for multiple languages**
- 📌 **Offline speech recognition** using CMU Sphinx
- 📌 **Integration with AI chatbots**

---

## 🤝 Contribution

Want to improve this project? Feel free to **fork, modify, and submit pull requests**! 🚀

---

## 📩 Contact

📧 Email: [Mail_me](mailto:iasma.channa@gmail.com)  
🔗 GitHub: [my_github](https://github.com/asma-13)  
🔗 LinkedIn: [my_linkedin](https://linkedin.com/in/iasmachanna)
