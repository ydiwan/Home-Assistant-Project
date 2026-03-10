import speech_recognition as sr

def continuous_speech_to_text():
    r = sr.Recognizer()
    r.pause_threshold = 2.0 
    
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        r.adjust_for_ambient_noise(source, duration=2)   
        r.energy_threshold = 300 
        r.dynamic_energy_threshold = False 
        
        print("\nReady! Speak into your microphone. (Say 'quit' or 'exit' to stop)")
        
        while True:
            print("\nListening...")
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=20)
                print("Processing...")
                
                text = r.recognize_google(audio).lower()
                print(f"[SUCCESS] You said: '{text}'")
                
                if "quit" in text or "exit" in text:
                    print("Stopping the speech recognition. Goodbye!")
                    break
                    
            except sr.WaitTimeoutError:
                pass 
            except sr.UnknownValueError:
                print("[ERROR] Could not understand the audio.")
            except sr.RequestError as e:
                print(f"[ERROR] API request failed; {e}")
            except KeyboardInterrupt:
                print("\nManual stop detected. Exiting...")
                break

if __name__ == "__main__":
    continuous_speech_to_text()