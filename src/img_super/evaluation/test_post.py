# -*- coding: utf-8 -*-
import argparse
import base64
import json
import requests
import datetime
from PIL import Image

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def send_image(image_path, service_url):
    encoded_image = encode_image(image_path)
    payload = {
        "image": f"data:image/jpeg;base64,{encoded_image}"
    }
    start_time = datetime.datetime.now()
    response = requests.post(service_url, json=payload)
    print("time =", (datetime.datetime.now() - start_time).total_seconds())
    return response.json()

def crop_image(image_path, coords):
    image = Image.open(image_path)
    cropped_image = image.crop((coords["x_min"], coords["y_min"], coords["x_max"], coords["y_max"]))
    return cropped_image

def add_text_to_image(image, reco):
    from PIL import ImageDraw, ImageFont

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 30)  # Cambia la fuente y el tamaño según tus necesidades
    draw.text((10, 10), reco, font=font, fill=(255, 0, 0))  # Cambia la posición y el color del texto según tus necesidades

    return image

def main():
    parser = argparse.ArgumentParser(description="Enviar una imagen a un servicio FastAPI.")
    parser.add_argument("image_path", type=str, help="Ruta de la imagen a enviar.")
    parser.add_argument("service_url", type=str, help="URL del servicio FastAPI.")

    args = parser.parse_args()

    response = send_image(args.image_path, args.service_url)
    print(json.dumps(response, indent=2))

    if "coord" in response and "reco" in response:
        coords = response["coord"]
        reco = response["reco"]

        cropped_image = crop_image(args.image_path, coords)
        image_with_text = add_text_to_image(cropped_image, reco)

        image_with_text.show()

if __name__ == "__main__":
    main()
