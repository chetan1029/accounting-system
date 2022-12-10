import React, { useContext, useEffect } from 'react'
import TransactionContext from '../context/transactions/TransactionContext'
import TransactionHistoryItem from './TransactionHistoryItem'
import Alert from '../components/Alert'
import Loading from '../components/Loading'

const TransactionHistory = () => {
    const context = useContext(TransactionContext);
    const { transactions, getTransactions, alert, setAlert, loading } = context;

    useEffect(() => {
        getTransactions()
    }, [])


    useEffect(() => {
        setTimeout(() => {
            setAlert(null);
        }, 3000);
    }, [alert])

    return (
        <div className="lg:col-span-2">
            <div className="bg-white border-solid border border-slate-200 max-h-screen shadow rounded px-8 pt-6 pb-8 mb-4 overflow-y-auto scroll-smooth">
                <h5 className="text-xl font-semibold mb-5">Transaction history</h5>
                {loading && <Loading />}
                <Alert alert={alert} />
                <ul className="divide-y divide-slate-100">
                    {transactions.map((transaction, i) => {
                        return <TransactionHistoryItem key={i} account_id={transaction.account_id} amount={transaction.amount} balance={transaction.balance ? transaction.balance : null} />
                    })}
                </ul>
            </div>
        </div>
    )
}


export default TransactionHistory
