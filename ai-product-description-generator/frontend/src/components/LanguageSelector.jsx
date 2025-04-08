import React, { useState } from 'react';

const LanguageSelector = ({ onLanguageChange }) => {
    const [selectedLanguage, setSelectedLanguage] = useState('en');

    const handleLanguageChange = (event) => {
        const newLanguage = event.target.value;
        setSelectedLanguage(newLanguage);
        onLanguageChange(newLanguage);
    };

    return (
        <div className="language-selector">
            <label htmlFor="language" className="block text-sm font-medium text-gray-700">
                Select Language:
            </label>
            <select
                id="language"
                value={selectedLanguage}
                onChange={handleLanguageChange}
                className="mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring focus:ring-indigo-500"
            >
                <option value="en">English</option>
                <option value="ar">Arabic</option>
            </select>
        </div>
    );
};

export default LanguageSelector;