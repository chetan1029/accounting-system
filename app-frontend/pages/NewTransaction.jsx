import React, { useContext, useState } from 'react'
import TransactionContext from '../context/transactions/TransactionContext'
import TextInput from '../components/TextInput';
import { useFormik } from 'formik';
import * as Yup from 'yup';
import SubmitInput from '../components/SubmitInput';
import FormError from '../components/FormError';

const NewTransaction = () => {
    const context = useContext(TransactionContext);
    const { createTransaction } = context;

    // Formik Validation
    // Valid UUID V4 Regex ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}
    const validator = useFormik({
        initialValues: {
            account_id: '',
            amount: ''
        },
        validationSchema: Yup.object({
            account_id: Yup.string().required('Account ID is required').matches(
                /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/,
                "Must enter a valid UUID v4 Account ID"
            ),
            amount: Yup.number().required('Amount is required')
        }),
        onSubmit: (values, actions) => {
            // Create Transaction
            createTransaction(values.account_id, values.amount);
            // Clear Form
            actions.resetForm();
        },
    });

    return (
        <div className="">
            <form className="bg-white border-solid border border-slate-200 shadow rounded px-8 pt-6 pb-8 mb-4 " onSubmit={validator.handleSubmit}>
                <h5 className="text-xl font-semibold mb-5">Submit new transaction</h5>
                <div className="mb-4">
                    <TextInput
                        datatype="account-id"
                        id="account_id"
                        name='account_id'
                        onChange={validator.handleChange}
                        onBlur={validator.handleBlur}
                        value={validator.values.account_id}
                        placeholder="Enter Account ID"
                        label="Account ID"
                    />

                    {validator.touched.account_id && validator.errors.account_id ? (
                        <FormError error={validator.errors.account_id} />
                    ) : null}
                </div>

                <div className="mb-6">
                    <TextInput
                        datatype="amount"
                        id="amount"
                        name='amount'
                        onChange={validator.handleChange}
                        onBlur={validator.handleBlur}
                        value={validator.values.amount}
                        placeholder="Enter Amount"
                        label="Amount"
                    />

                    {validator.touched.amount && validator.errors.amount ? (
                        <FormError error={validator.errors.amount} />
                    ) : null}
                </div>
                <div className="flex items-center justify-between">
                    <SubmitInput datatype="transaction-submit" value="Submit" />
                </div>
            </form>
        </div>
    )
}


export default NewTransaction
