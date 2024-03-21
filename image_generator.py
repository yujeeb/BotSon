import replicate
import requests


class ImageGen():
    def __init__(self):
        self.waiting_for_img_prompt = False


    def generate_image(self, image_prompt):
        output = replicate.run(
        "lucataco/sdxl-lightning-4step:727e49a643e999d602a896c774a0658ffefea21465756a6ce24b7ea4165eba6a",
        input={
            "seed": 2992471961,
            "width": 1024,
            "height": 1024,
            "prompt": image_prompt,
            "scheduler": "K_EULER",
            "num_outputs": 1,
            "guidance_scale": 0,
            "negative_prompt": "worst quality, low quality",
            "num_inference_steps": 4
            }
        )

        print("Output:")
        print(output)

        output_url = output[0]

        self.download_img(output_url)


    def download_img(self, url):
        filename = "image.png"

        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Open a file in binary write mode and write the content of the response to it
            with open(filename, 'wb') as f:
                f.write(response.content)
            print("Image downloaded successfully!")
        else:
            print("Failed to download image. Status code:", response.status_code)
