import requests
import matplotlib.pyplot as plt

def main():

    temps = []
    for year in range(1942, 2021):
        response = requests.get(f"https://archive-api.open-meteo.com/v1/archive?latitude=52.23&longitude=21.01&start_date={str(year)}-01-01&end_date={str(year)}-12-31&daily=temperature_2m_mean&timezone=Europe%2FBerlin")
        temp = response.json().get('daily').get('temperature_2m_mean')
        temps.append(average(temp))
        print(year)

    plt.plot(range(1942, 2021), temps)
    plt.show()

def average(nums):
    total = 0
    for num in nums:
        total += num
    return total/len(nums)
    

if __name__ == "__main__":
    main()
