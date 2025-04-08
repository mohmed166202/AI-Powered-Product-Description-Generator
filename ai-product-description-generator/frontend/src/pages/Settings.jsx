import React, { useState } from 'react';

const Settings = () => {
    const [language, setLanguage] = useState('en');
    const [tone, setTone] = useState('neutral');
    const [keywords, setKeywords] = useState('');

    const handleLanguageChange = (e) => {
        setLanguage(e.target.value);
    };

    const handleToneChange = (e) => {
        setTone(e.target.value);
    };

    const handleKeywordsChange = (e) => {
        setKeywords(e.target.value);
    };

    const handleSaveSettings = () => {
        // Logic to save settings (e.g., API call)
        console.log('Settings saved:', { language, tone, keywords });
    };

    return (
        <div className="settings-container">
            <h1 className="text-2xl font-bold">Settings</h1>
            <div className="mt-4">
                <label className="block mb-2">Language</label>
                <select value={language} onChange={handleLanguageChange} className="border p-2">
                    <option value="en">English</option>
                    <option value="ar">Arabic</option>
                </select>
            </div>
            <div className="mt-4">
                <label className="block mb-2">Tone</label>
                <select value={tone} onChange={handleToneChange} className="border p-2">
                    <option value="neutral">Neutral</option>
                    <option value="friendly">Friendly</option>
                    <option value="professional">Professional</option>
                </select>
            </div>
            <div className="mt-4">
                <label className="block mb-2">Keywords</label>
                <input
                    type="text"
                    value={keywords}
                    onChange={handleKeywordsChange}
                    className="border p-2 w-full"
                    placeholder="Enter keywords separated by commas"
                />
            </div>
            <button onClick={handleSaveSettings} className="mt-4 bg-blue-500 text-white p-2 rounded">
                Save Settings
            </button>
        </div>
    );
};

export default Settings;