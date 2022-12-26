import React from 'react'
import Article from '../components/Article'
import PropTypes from 'prop-types'

const TransactionHistoryItem = (props) => {
    const {
        amount,
        account_id,
        balance
    } = props
    return (
        <Article
            datatype="transaction"
            amount={amount}
            account_id={account_id}
            balance={balance}
        />
    )
}

TransactionHistoryItem.propTypes = {
    amount: PropTypes.number,
    account_id: PropTypes.string,
    balance: PropTypes.number
}

export default TransactionHistoryItem
