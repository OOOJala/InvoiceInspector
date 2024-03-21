Install (if needed) Python (Anaconda) to your Windows desktop
Modify value of path-variable in .py-file

invoices.csv
 -All invoices you have sent to your customers
 [Name] [SUM] [Reference Number]

transactions.csv
 - Transaction report from Bank service
 [Reference Number] [Type of transaction] [Paid SUM]

invoiceInspector.py
 - Reads invoices
 - Compares referencenumbers
 - Compares payed sums
 - Creates a report.csv where reported paid and unpaid invoices and amounts
