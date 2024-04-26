from abstractpets import Animal,Birds,Shree

def main():
    animal=Animal(color= "Orange",num_types= 7,sound ="large")
    birds=Birds(color= "Green",num_types= 5,sound="medium")
    shree=Shree(color ="Gold",num_types= 3,sound="loud")
    
    animal.display_details()
    print("\n")
    birds.display_details()
    print("\n")
    shree.display_details()
    
    
if __name__=="__main__":
    main()
                  

