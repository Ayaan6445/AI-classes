import requests
from PIL import Image
from io import BytesIO
from Config import HF_API_KEY

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

def generate_image(prompt):
    payload = {
        "inputs": prompt
    }

    response = requests.post(API_URL, headers=headers, json=payload, timeout=60)

    if response.status_code != 200:
        print("Error generating image")
        return None

    image = Image.open(BytesIO(response.content))
    return image

def main():
    print("🖼️ Text to Image Generator")
    print("Type 'exit' to quit")

    while True:
        prompt = input("\nEnter image description: ")

        if prompt.lower() == "exit":
            print("Goodbye 👋")
            break
        image = generate_image(prompt)
        if image:
            image.show()
            save = input("Do you want to save the image? (yes/no): ").lower()
            if save == "yes":
                filename = input("Enter your file name: ")
                image.save(f"{filename}.png")
                print("✅ Image saved succesfully")

if __name__ == "__main__":
    main()