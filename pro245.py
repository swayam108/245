from web3 import Web3
from tkinter import *
root = Tk()

root.title("My Ethereum App")
root.geometry("500x200")
root.configure(background="white")

# Setting labels
block_name_label = Label(root, text="Ethereum Block", font=("Helvetica", 18, 'bold'), bg="white")
block_name_label.place(relx=0.5, rely=0.15, anchor=CENTER)
block_entry = Entry(root, text="This is Entry Widget", bd=2)

block_entry.place(relx=0.5, rely=0.35, anchor=CENTER)
gasused_info_label = Label(root, bg="white", font=("bold", 10))
gasused_info_label.place(relx=0.5, rely=0.38, anchor=CENTER)
gaslimit_info_label = Label(root, bg="white", font=("bold", 10))
gaslimit_info_label.place(relx=0.5, rely=0.5, anchor=CENTER)


API_url ='https://mainnet.infura.io/v3/ec5acb1175dc468c9f3ee9a84a02fe98'
web3 = Web3(Web3.HTTPProvider(API_url))

# Write Code for Task 01 below.
def ethereum_block():
    number = int(block_entry.get())
    block_data = web3.eth.get_block(number)
    
    transactions = block_data['transactions']
    if transactions:
        transaction_hash = transactions[0]  # Assuming the first transaction in the block
        transaction = web3.eth.get_transaction(transaction_hash)
        
        value = transaction['value']
        value_in_ether = value / 10**18
        value_in_dollar = value_in_ether * 2399.82

        # Task 01: Update 'text' parameter of gasused_info_label
        gasused_info_label["text"] = "Value: $" + str(value_in_dollar)

        # Task 02: Update 'text' parameter of gaslimit_info_label
        gaslimit_info_label["text"] = "Gas: " + str(transaction['gas'])

        # Task 03: Update 'text' parameter of block_name_label
        block_name_label["text"] = block_entry.get()

        block_entry.destroy()
        search_btn.destroy()
    else:
        # Handle case when there are no transactions in the block
        print("No transactions in the block")

search_btn = Button(root, text="Search Ethereum transaction fee", command=ethereum_block, relief=FLAT)
search_btn.place(relx=0.5, rely=0.48, anchor=CENTER)
root.mainloop()
