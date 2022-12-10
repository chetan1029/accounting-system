import React from 'react'
import PropTypes from 'prop-types'

const Alert = (props) => {
    const alertClass = {
        "error": "text-red-700 bg-red-100",
        "success": "text-green-700 bg-green-100"
    }
    const {
        alert
    } = props
    return (
        <>
            {
                alert && Object.keys(alert).length !== 0 && <div className={`p-4 mb-4 text-sm ${alertClass[alert.type]} rounded-lg`} role="alert">
                    <span className="font-medium"> {alert?.type?.toUpperCase()}!</span> {alert.message}
                </div>
            }
        </>
    )
}

Alert.propTypes = {
    alert: PropTypes.object
}

export default Alert
