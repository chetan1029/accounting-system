import Article from "../components/Article";
import { render } from '@testing-library/react'

describe(Article, () => {
    it("Testing transaction detail if we give transfer to the account", () => {
        const { getByTestId } = render(
            <Article
                datatype="transaction"
                amount={200}
                account_id={"123A-123B-123C"}
                balance={null}
            />
        );
        const transactionDetail = getByTestId("transaction_detail").textContent;
        expect(transactionDetail).toEqual("Transfered 200$ to account 123A-123B-123C");
    });

    it("Testing transaction detail if we give transfer from the account", () => {
        const { getByTestId } = render(
            <Article
                datatype="transaction"
                amount={-200}
                account_id={"123A-123B-123C"}
                balance={null}
            />
        );
        const transactionDetail = getByTestId("transaction_detail").textContent;
        expect(transactionDetail).toEqual("Transfered 200$ from account 123A-123B-123C");
    });

    it("Testing if account detail exist", () => {
        const { getByTestId } = render(
            <Article
                datatype="transaction"
                amount={-200}
                account_id={"123A-123B-123C"}
                balance={1000}
            />
        );
        const accountDetail = getByTestId("account_detail").textContent;
        expect(accountDetail).toEqual("The current account balance is 1000$");
    });

    it("Testing if account detail doesn't exist", () => {
        const { queryByTestId } = render(
            <Article
                datatype="transaction"
                amount={-200}
                account_id={"123A-123B-123C"}
                balance={null}
            />
        );
        const accountDetail = queryByTestId("account_detail");
        expect(accountDetail).toBeNull();
    });

    it("test data-type attribute", () => {
        const { queryByTestId } = render(
            <Article
                datatype="transaction"
                amount={-200}
                account_id={"123A-123B-123C"}
                balance={null}
            />
        );
        const accountDetail = queryByTestId("transaction_block");
        expect(accountDetail.getAttribute("data-type")).toEqual("transaction");
    });

    it("test data-account-id attribute", () => {
        const { queryByTestId } = render(
            <Article
                datatype="transaction"
                amount={-200}
                account_id={"123A-123B-123C"}
                balance={null}
            />
        );
        const accountDetail = queryByTestId("transaction_block");
        expect(accountDetail.getAttribute("data-account-id")).toEqual("123A-123B-123C");
    });

    it("test data-amount attribute", () => {
        const { queryByTestId } = render(
            <Article
                datatype="transaction"
                amount={-200}
                account_id={"123A-123B-123C"}
                balance={null}
            />
        );
        const accountDetail = queryByTestId("transaction_block");
        expect(accountDetail.getAttribute("data-amount")).toEqual("-200");
    });

    it("test data-balance attribute", () => {
        const { queryByTestId } = render(
            <Article
                datatype="transaction"
                amount={-200}
                account_id={"123A-123B-123C"}
                balance={1000}
            />
        );
        const accountDetail = queryByTestId("transaction_block");
        expect(accountDetail.getAttribute("data-balance")).toEqual("1000");
    });

});