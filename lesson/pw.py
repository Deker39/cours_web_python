                                                                                                                             
num2words1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \                                                        
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \                                                        
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \                                                    
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}                                   
num2words2 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']                                  
                                                                                                                             
def number(bal):                                                                                                             
    if 1 <= bal < 19:                                                                                                        
        return num2words1[bal]                                                                                               
    elif 20 <= bal <= 99:                                                                                                    
        tens = bal//10                                                                                                       
        below_ten = bal%10                                                                                                   
        if below_ten == 0:                                                                                                   
            return num2words2[tens-2]                                                                                        
        else: return num2words2[tens-2] + '-' + num2words1[below_ten]                                                        
    else:                                                                                                                    
        print("Number out of range")                                                                                         
                                                                                                                             
                                                                                                                             
                                                                                                                             
balans = input("Enter your balans: ")  # баланс от 0 до 100                                                                  
print(f'Your balanse:{balans}$, please make a choice')                                                                       
print(f'Num 1: Americano - 10$\n'                                                                                            
      f'Num 2: Americano with milk - 12$\n'                                                                                  
      f'Num 3: Latte - 15$\n'                                                                                                
      f'Num 4: Cappuccino -20$\n'                                                                                            
      f'Num 5: Espresso- 6%\n')                                                                                              
                                                                                                                             
choice = int(input("Choice: "))                                                                                              
                                                                                                                             
if not choice or len(balans) > 3 or 1 <= choice >6: print('You don\'t make a choice')                                        
else:                                                                                                                        
    if int(balans) > choice:                                                                                                 
         if choice == 1: print(f'your order: Americano\nyour change: {int(balans) -10}-{number(int(balans) -10)}')           
         elif choice == 2: print(f'your order:Americano with milk\nyour change: {int(balans) -12}-{number(int(balans) -12)}')
         elif choice == 3: print(f'your order: Latte\nyour change: {int(balans) -15}-{number(int(balans) -15)}')             
         elif choice == 4: print(f'your order: Cappuccino\nyour change: {int(balans) -20}-{number(int(balans) -20)}')        
         elif choice == 5: print(f'your order: Espresso\nyour chang: {int(balans) - 6}-{number(int(balans) - 6)}')           
    else: print('you poor')                                                                                                  
                                                                                                                             