import React from 'react'
import PropTypes from 'prop-types'

const FormError = (props) => {
    const {
        error
    } = props
    return (
        <p className="text-red-500 text-xs italic">{error}</p>
    )
}

FormError.propTypes = {
    error: PropTypes.string
}

export default FormError
