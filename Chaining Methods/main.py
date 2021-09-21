from User import User

pedroAccount = User( 12345, "Pedro Sanchez" )
julianAccount = User( 22222, "Julian Alvarez" )
amandaAccount = User( 54321, "Amanda Thriller" )

# print (User.allUsersaccounts)

julianAccount.deposit_acc(50000).printUsersinfo()


amandaAccount.deposit_acc(1000).withdraw_acc(500).printUsersinfo()



pedroAccount.deposit_acc(5000).withdraw_acc(1000).printUsersinfo()




