import React from 'react'
import PropTypes from 'prop-types'

const Article = (props) => {
    const {
        datatype,
        amount,
        account_id,
        balance
    } = props

    return (
        <article className="flex items-start space-x-6 py-3">
            <div className="min-w-0 relative flex-auto" data-testid="transaction_block" data-type={datatype} data-account-id={account_id} data-amount={amount} data-balance={balance}>
                <div className="text-slate-900 pr-20" data-testid="transaction_detail">
                    Transfered {Math.abs(amount)}$ {amount < 0 ? 'from' : 'to'} account {account_id}
                </div>
                {balance ? <h2 className="text-slate-900 pr-20 mt-2" data-testid="account_detail">The current account balance is {balance}$</h2> : ''}
            </div>
        </article>
    )
}

Article.propTypes = {
    datatype: PropTypes.string,
    amount: PropTypes.number,
    account_id: PropTypes.string,
    balance: PropTypes.number
}

export default Article
