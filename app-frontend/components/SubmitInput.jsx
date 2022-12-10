import React from 'react'
import PropTypes from 'prop-types'

const SubmitInput = (props) => {
    const {
        datatype,
        value
    } = props
    return (
        <>
            <input
                className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline cursor-pointer"
                type="submit"
                data-type={datatype}
                value={value}
            />
        </>
    )
}

SubmitInput.propTypes = {
    datatype: PropTypes.string,
    value: PropTypes.string
}

export default SubmitInput