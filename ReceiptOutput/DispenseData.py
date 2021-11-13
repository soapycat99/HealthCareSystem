import ReceiptOutput.Receipt as rc

def dispenseReceipt(amount,des):
    receipt = rc.Receipt(amount,des)
    return receipt.getReceipt()