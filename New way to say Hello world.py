def gradual_print(text):
    for i in range(1, len(text) + 1):
        print(text[:i])

if __name__ == "__main__":
    gradual_print("hello world")
