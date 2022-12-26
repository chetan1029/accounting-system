import TransactionContext from "./TransactionContext";
import { useState } from "react";

const TransactionState = (props) => {
    const host = "http://127.0.0.1:8000";
    const transactionsInitial = []
    const [transactions, setTransactions] = useState(transactionsInitial)
    const [alert, setAlert] = useState({})
    const [loading, setLoading] = useState(true)

    // Get all Transactions
    const getTransactions = async () => {
        // API Call 
        setLoading(true)
        try {
            const response = await fetch(`${host}/api/accounting/transactions`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            if (!response.ok) {
                throw Error(response.statusText);
            }
            const transactionsJson = await response.json()
            if (transactionsJson) {
                const account = await getAccount(transactionsJson[0].account_id)
                transactionsJson[0]["balance"] = account.balance
            }
            setTransactions(transactionsJson)
            setLoading(false)
        } catch (error) {
            setAlert({ type: "error", message: error.message })
            setLoading(false)
        }

    }

    // Get Account by account id
    const getAccount = async (account_id) => {
        // API Call 
        try {
            const response = await fetch(`${host}/api/accounting/accounts/${account_id}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            if (!response.ok) {
                throw Error(response.statusText);
            }
            const accountJson = await response.json()
            return accountJson
        } catch (error) {
            setAlert({ type: "error", message: error.message })
        }

    }

    // Create a new transaction
    const createTransaction = async (account_id, amount) => {
        // API Call 
        setLoading(true)
        try {
            const response = await fetch(`${host}/api/accounting/transactions`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ account_id, amount })
            });
            if (response.ok) {
                const json = await response.json()
                await getTransactions()
                setAlert({ type: "success", message: "Transaction added successfully" })
                setLoading(false)
            } else if (response.status === 400) {
                const json = await response.json()
                setAlert({ type: "error", message: json.errors.join(", ") })
                setLoading(false)
            } else {
                throw Error(response.error);
            }
        } catch (error) {
            setAlert({ type: "error", message: error.message })
            setLoading(false)
        }
    }

    return (
        <TransactionContext.Provider value={{ transactions, alert, getTransactions, createTransaction, setAlert, loading }}>
            {props.children}
        </TransactionContext.Provider>
    )
}

export default TransactionState;