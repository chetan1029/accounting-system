import React, { useContext, useEffect } from 'react'
import NewTransaction from './NewTransaction'
import TransactionHistory from './TransactionHistory'

const Transactions = () => {

    return (
        <>
            <main className="w-full px-20">
                <div className="grid mt-3 mb-5">
                    <h1 className="text-4xl font-bold text-center">
                        Transactions System
                    </h1>
                </div>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3 mt-5 h-screen">
                    <NewTransaction />
                    <TransactionHistory />
                </div>
            </main>
        </>
    )
}


export default Transactions
