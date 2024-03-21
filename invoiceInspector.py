path = '/path/to/the/file/'

with open(path+'invoices.csv','r') as invoiceCsvfile, open(path+'transactions.csv','r') as transactionCsvfile:
    invoiceReader = invoiceCsvfile.readlines()
    transactionReader = transactionCsvfile.readlines()

    #print(invoiceReader[1].split(";"))

    p=0;
    paidInvoices = []
    unpaidInvoices = []

    #Check if the incoice is paid
    for invoiceRow in invoiceReader:
        pBeginning = p
        invoiceRowList = invoiceRow.split(";")
        refInInvoice = invoiceRowList[2].replace("\n","")
        sumInInvoice = float(invoiceRowList[1].replace(",","."))
        for transactionRow in transactionReader: 
            transactionRowList = transactionRow.split(";")
            refInTransaction = transactionRowList[0].replace(" ", "")
            sumInTransaction = float(transactionRowList[2].replace("\n", ""))
            if not refInTransaction.isnumeric():
                dirtyRefList = list(refInTransaction)
                refInTransaction = ''
                for dirtyRefUnit in dirtyRefList:
                    if dirtyRefUnit.isnumeric():
                        refInTransaction += dirtyRefUnit

                
            if refInInvoice == refInTransaction:
                if sumInInvoice == sumInTransaction:
                    paidInvoices.append(invoiceRowList[0]+";"+refInInvoice+";OK\n")
                else:
                    paidInvoices.append(invoiceRowList[0]+";"+refInInvoice+";OK but "+ str(sumInInvoice) +" <> "+ str(sumInTransaction)+"\n")
                    
                p += 1
        #Invoice is unpaid
        if pBeginning == p:
            unpaidInvoices.append(invoiceRowList[0]+";"+refInInvoice+";UNPAID\n")

    
    reportFile = open(path+'report.csv', 'w')
    reportFile.write("Name;Ref.No;Status\n")
    reportFile.write("===================\n")
    for paid in paidInvoices:
        reportFile.write(paid)
        
    reportFile.write("\nPAID;"+str(len(paidInvoices)))
    reportFile.write("\n\n")

    for unpaid in unpaidInvoices:
        reportFile.write(unpaid)

    reportFile.write("\nUNPAID;"+str(len(unpaidInvoices)))

    reportFile.close()
