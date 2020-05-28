                self.previous_state = 0
            time.sleep(3)               

    def pause(self):
        self.enpause = True
        print("thread en pause...")

    def reprise(self):
        self.enpause = False
        print("reprise thread...")

    def stop(self):
        self.encore = False


mon_thread = Monthread()
mon_thread.start()

try:
    while True:
        time.sleep(0.5)    
        if mon_thread.isAlive() and motion:
            mon_thread.pause()
            
            print("Open pump")
            GPIO.output(relay_pin, GPIO.HIGH)
            time.sleep(0.005)

            print("Pump stopped")
            GPIO.output(relay_pin, GPIO.LOW)
            motion = False
            time.sleep(10)
            mon_thread.reprise()

except KeyboardInterrupt:
    print("CTRL-C: Terminating program.")
finally:
    print("Cleaning up GPIO...")
    mon_thread.stop() 
    GPIO.output(relay_pin, GPIO.LOW)
    GPIO.cleanup()

