from  datetime import timedelta,date
class bus:
    def __init__(self):
        try :
            file = open('steats.txt', 'r')
        except FileNotFoundError:
            file = open('steats.txt', 'w')
            x = 0
            while x < 7:
                file.write("0 0 0 0"+'\n')
                x +=1
            file.close()
        bus.handel_selection()
    def handel_selection():
        print("---------- Welcome to Bus Seat Reservation System ***","Date | ", date.today(),"----------\n" )
        while True:

            print('1) Display a number for available seats.')
            print('2) Display status of all seats.')
            print('3) Reserve seats.')
            print('4) Delete reservation.' )
            print('5) Exit. ')
            print("************************************************************************************")

            ui = input('Enter your choice : ')
            if ui == '1':
                bus.available_seats()
                bus.continue_reservation()
            elif ui == '2':
                bus.seats_status()
                bus.continue_reservation()
            elif ui == '3':
                bus.seats_status()
                bus.reserve_seats()
                bus.continue_reservation()
            elif ui == '4':
                bus.seats_status()
                bus.delete_reservation()
                bus.continue_reservation()
            elif ui == '5':
                print('logout successfully')
                break
            else:
                print('Invalid input, Please enter a number according to this list [1,2,3,4,5]')
                bus.continue_reservation() 
    def available_seats():
            lot = list() # list_of_txt
            fhandel = open('steats.txt','r')
            for line in fhandel:
                for i in line.split() :
                    lot.append(i)
            fhandel.close()
            print('There are' , lot.count('0') , 'available seats.')
            print('There are' , lot.count('1') ,  'non-available seats.')
    def seats_status():
            seats = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
            lot = list() # list_of_txt
            fhandel = open('steats.txt','r')
            for line in fhandel:
                for i in line.split() :
                    lot.append(i)
            fhandel.close()
            for i in range(len(lot)): 
                if (lot[i]) == '1':
                    seats[i] = 'reserved'
            print('{   ',seats[0],'   }' , '{   ',seats[1],'   }' , '{   ',seats[2],'   }' , '{   ',seats[3],'   }\n' )
            print('{   ',seats[4],'   }' , '{   ',seats[5],'   }' , '{   ',seats[6],'   }' , '{   ',seats[7],'   }\n' )
            print('{   ',seats[8],'   }' , '{   ',seats[9],'  }' ,'{   ',seats[10],'  }' , '{  ',seats[11],'   }\n' )
            print('{   ',seats[12],'  }' , '{   ',seats[13],'  }' , '{   ',seats[14],'  }' , '{   ',seats[15],'  }\n' )
            print('{   ',seats[16],'  }' , '{   ',seats[17],'  }' , '{   ',seats[18],'  }' , '{   ',seats[19],'  }\n' )
            print('{   ',seats[20],'  }' , '{   ',seats[21],'  }' , '{   ',seats[22],'  }' , '{   ',seats[23],'  }\n' )
            print('{   ',seats[24],'  }' , '{   ',seats[25],'  }' , '{   ',seats[26],'  }' , '{   ',seats[27],'  }\n' )
    def reserve_seats():
        lot = list() # list_of_txt
        fhandel = open('steats.txt','r')
        for line in fhandel:
            for i in line.split() :
                lot.append(i)
        fhandel.close()
        seats = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
        availabl_counter = lot.count('0')
        non_availabl_counter = lot.count('1')
        if availabl_counter == 0:
            print('Sorry, there are no available seats')
        else :
            print('There are ' + str(availabl_counter) + ' available seats, and there are ' 
            + str(non_availabl_counter) + ' seats are reserved' )
            try :
                userInput = int(input('how much seats do you want? '))
                if userInput <= 0 :
                    print('invalid number, Please enter a number bigger than 0')
                elif userInput > availabl_counter : 
                    print('sorry, there are no '+ str(userInput) + ' seats are availabl.')
                else :
                    x = 1 
                    while x <= userInput:
                            ui = int(input('choice a seat number '+ str(x) + ": "))
                            if ui <= 0 or ui > 28:
                                print('invalid number, Please enter a number bigger than 0 and smaller than 28')
                            elif lot[seats.index(ui)] == '1' :
                                print('sorry, the seat is reserved')
                            else:
                                lot[seats.index(ui)] = '1'
                                x +=1
                    print('Reserve successfully, Have a good day!')
            except: print('invalid input, Please enter a number ')
            fhandel = open('steats.txt','w')
            fhandel.write(lot[int(0)]+' ' + lot[int(1)]+' ' +lot[int(2)]+' ' +lot[int(3)]+'\n')
            fhandel.write(lot[int(4)]+' ' +lot[int(5)]+' ' +lot[int(6)]+' ' +lot[int(7)]+'\n')
            fhandel.write(lot[int(8)]+' ' +lot[int(9)]+' ' +lot[int(10)]+' ' +lot[int(11)]+'\n')
            fhandel.write(lot[int(12)]+' ' +lot[int(13)]+' ' +lot[int(14)]+' ' +lot[int(15)]+'\n')
            fhandel.write(lot[int(16)]+' ' +lot[int(17)]+' ' +lot[int(18)]+' ' +lot[int(19)]+'\n')
            fhandel.write(lot[int(20)]+' ' +lot[int(21)]+' ' +lot[int(22)]+' ' +lot[int(23)]+'\n')
            fhandel.write(lot[int(24)]+' ' +lot[int(25)]+' ' +lot[int(26)]+' ' +lot[int(27)]+'\n')
            fhandel.close()
    def delete_reservation():
            lot = list() # list_of_txt
            fhandel = open('steats.txt','r')
            for line in fhandel:
                for i in line.split() :
                    lot.append(i)
            fhandel.close()
            seats = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
            availabl_counter = lot.count('0')
            non_availabl_counter = lot.count('1')
            if availabl_counter == 28:
                print('Sorry, There are no reserved seats')
            else :
                print('There are ' + str(availabl_counter) + ' available seats, and there are ' 
                + str(non_availabl_counter) + ' seats are reserved' )
                try :
                    userInput = int(input('how much seats do you want to delete? '))
                    if userInput <= 0 :
                            print('invalid number, Please enter a number bigger than 0')
                    elif userInput > non_availabl_counter : 
                            print('sorry, there are no '+ str(userInput) + ' seats reserved.')
                    else :
                        x = 1 
                        while x <= userInput:
                            ui = int(input('choice a seat number '+ str(x) + ": "))
                            if ui <= 0 or ui > 28:
                                print('invalid number, Please enter a number bigger than 0 and smaller than 28')
                            elif lot[seats.index(ui)] == '0' :
                                print('sorry, the seat is not reserved')
                            else:
                                lot[seats.index(ui)] = '0'
                                x +=1
                        print('Reservation has been canceled successfully, Have a good day!')
                except: print('invalid input, Please enter a number ')
            fhandel = open('steats.txt','w')
            fhandel.write(lot[int(0)]+' ' + lot[int(1)]+' ' +lot[int(2)]+' ' +lot[int(3)]+'\n')
            fhandel.write(lot[int(4)]+' ' +lot[int(5)]+' ' +lot[int(6)]+' ' +lot[int(7)]+'\n')
            fhandel.write(lot[int(8)]+' ' +lot[int(9)]+' ' +lot[int(10)]+' ' +lot[int(11)]+'\n')
            fhandel.write(lot[int(12)]+' ' +lot[int(13)]+' ' +lot[int(14)]+' ' +lot[int(15)]+'\n')
            fhandel.write(lot[int(16)]+' ' +lot[int(17)]+' ' +lot[int(18)]+' ' +lot[int(19)]+'\n')
            fhandel.write(lot[int(20)]+' ' +lot[int(21)]+' ' +lot[int(22)]+' ' +lot[int(23)]+'\n')
            fhandel.write(lot[int(24)]+' ' +lot[int(25)]+' ' +lot[int(26)]+' ' +lot[int(27)]+'\n')
            fhandel.close()
    def continue_reservation():
        input('Press enter key to continue ')
        print('----------------------------')      
bus()                        


