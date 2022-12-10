import React from 'react'
import PropTypes from 'prop-types'

const TextInput = (props) => {
    const {
        datatype,
        id,
        name,
        onChange,
        onBlue,
        value,
        placeholder,
        label = ""
    } = props
    return (
        <>
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor={id}>
                {label}
            </label>
            <input
                data-type={datatype}
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
                id={id}
                name={name}
                type="text"
                onChange={onChange}
                onBlur={onBlue}
                value={value}
                placeholder={placeholder} />
        </>
    )
}

TextInput.propTypes = {
    datatype: PropTypes.string,
    id: PropTypes.string,
    name: PropTypes.string,
    onChange: PropTypes.func,
    onBlue: PropTypes.func,
    value: PropTypes.string,
    placeholder: PropTypes.string,
    label: PropTypes.string
}

export default TextInput