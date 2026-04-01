import requests
from bs4 import BeautifulSoup

def get_turbo_prices():
    print("Turbo.az-da axtarış aparılır...")
    
    # Yeni axtarış linki (Hyundai Sonata 2008, 2.0L)
    url = "https://turbo.az/autos?q%5Bmake%5D%5B%5D=6&q%5Bmodel%5D%5B%5D=59&q%5Byear_from%5D=2008&q%5Byear_to%5D=2008&q%5Bmotor_size_from%5D=2000&q%5Bmotor_size_to%5D=2000"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "az,ru;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Sayta daxil olmaq mümkün olmadı. Xəta kodu: {response.status_code}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Turbo.az-da qiymətlər bəzən 'tz-container' daxilində 'products-i__price' class-ında olur
        # Biz bütün mümkün qiymət bloklarını yoxlayırıq
        prices = []
        
        # Əsas qiymət class-ı adətən budur:
        price_tags = soup.find_all(class_='product-price') 
        if not price_tags:
            # Əgər yuxarıdakı tapılmasa, bu class-ı yoxla:
            price_tags = soup.find_all(class_='products-i__price')

        for tag in price_tags:
            text = tag.get_text().strip()
            # "15 500 AZN" -> "15500"
            clean_price = "".join(filter(str.isdigit, text))
            if clean_price:
                prices.append(int(clean_price))

        if prices:
            avg = sum(prices) / len(prices)
            print("\n" + "="*40)
            print(f"Analiz nəticəsi (Hyundai Sonata 2008, 2.0L):")
            print(f"Tapılan elan: {len(prices)} ədəd")
            print(f"Ən ucuz: {min(prices)} AZN")
            print(f"Ən baha: {max(prices)} AZN")
            print(f"ORTALAMA QİYMƏT: {round(avg)} AZN")
            print("="*40)
        else:
            print("Təəssüf, heç bir qiymət tapılmadı.")
            print("İpucu: Brauzerdə Turbo.az-a girib baxın, bəlkə hazırda bu kriteriyada elan yoxdur?")

    except Exception as e:
        print(f"Gözlənilməz xəta: {e}")

# İcra et
get_turbo_prices()