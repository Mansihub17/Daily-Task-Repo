#Create a dictionary of movies as key and cast as value
#movies: cast
movies = {
    "3 Idiots": ["Aamir Khan", "R. Madhavan", "Sharman Joshi", "Kareena Kapoor Khan"],
    
    "Zindagi Na Milegi Dobara": ["Hrithik Roshan", "Farhan Akhtar", "Abhay Deol", "Katrina Kaif"],
    
    "Dil Chahta Hai": ["Aamir Khan", "Saif Ali Khan", "Akshaye Khanna", "Preity Zinta"],
    
    "Dangal": ["Aamir Khan", "Fatima Sana Shaikh", "Sanya Malhotra", "Sakshi Tanwar"],
    
    "Kal Ho Naa Ho": ["Shah Rukh Khan", "Preity Zinta", "Saif Ali Khan", "Jaya Bachchan"],
    
}
for movie, cast in movies.items():
print(movie,cast)