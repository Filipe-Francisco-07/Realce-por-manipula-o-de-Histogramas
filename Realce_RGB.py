import numpy as np
import matplotlib.pyplot as plt

def inserirImagem(arquivo):
    with open(arquivo, 'r') as f:
        cabecalho = f.readline().strip()
        dimensoes = f.readline().strip()
        maiorvalor = int(f.readline().strip())
        pixels = []
        for line in f:
            pixels.extend(map(int, line.split()))
    largura, altura = map(int, dimensoes.split())
    return cabecalho, largura, altura, maiorvalor, pixels

def write(arquivo, cabecalho, largura, altura, maiorvalor, pixels):
    with open(arquivo, 'w') as f:
        f.write(f"{cabecalho}\n{largura} {altura}\n{maiorvalor}\n")
        for i in range(altura):
            f.write(" ".join(map(str, pixels[i * largura * 3:(i + 1) * largura * 3])) + "\n")

def findMinMax(pixels,xMin,xMax):
    for pixel in pixels:
        if(pixel < xMin):
            xMin = pixel
        
        if(pixel > xMax):
            xMax = pixel
        
    return xMin, xMax

def resize_image_rgb(pixels,a,b):
    new_pixels = []
    for pixel in pixels:
       new_pixel =  a * pixel + b
       new_pixels.append(new_pixel)

    return new_pixels

def resize_and_save(input_arquivo, output_arquivo):
    cabecalho, largura, altura, maiorvalor, pixels = inserirImagem(input_arquivo)
    xMin = 255
    xMax = 0
    xMin, xMax = findMinMax(pixels,xMin,xMax)
    a = (255 / (xMax - xMin))
    b = (((-1)*(a))*xMin)
    new_pixels = resize_image_rgb(pixels, a, b)
    write(output_arquivo, cabecalho, largura, altura, maiorvalor, new_pixels)
    dados = np.array(new_pixels, dtype=int).reshape((altura, largura, 3))
    histograma(dados)

def histograma(dados):
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.hist(dados[..., 0].ravel(), bins=256, color='red', alpha=0.7, edgecolor='black')
    plt.title("Histograma RED")
    plt.xlabel("Número do pixel")
    plt.ylabel("Frequência")

    plt.subplot(1, 3, 2)
    plt.hist(dados[..., 1].ravel(), bins=256, color='green', alpha=0.7, edgecolor='black')
    plt.title("Histograma GREEN")
    plt.xlabel("Número do pixel")
    plt.ylabel("Frequência")

    plt.subplot(1, 3, 3)
    plt.hist(dados[..., 2].ravel(), bins=256, color='blue', alpha=0.7, edgecolor='black')
    plt.title("Histograma BLUE")
    plt.xlabel("Número do pixel")
    plt.ylabel("Frequência")

    plt.tight_layout()
    plt.show()

    plt.show()

# Entrando com a imagem inicial
arquivo_entrada = 'c:/Users/jukal/Desktop/HistogramaPDI/EntradaRGB.ppm'
resize_and_save(arquivo_entrada, 'c:/Users/jukal/Desktop/HistogramaPDI/Realce_ImagemRGB.pgm')
