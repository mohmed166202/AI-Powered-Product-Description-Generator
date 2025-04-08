import React from 'react';
import LanguageSelector from '../components/LanguageSelector';

const Home = () => {
    return (
        <div className="flex flex-col items-center justify-center h-screen">
            <h1 className="text-4xl font-bold mb-4">AI-Powered Product Description Generator</h1>
            <LanguageSelector />
            <p className="text-lg mt-4">Generate compelling product descriptions in English and Arabic.</p>
            <div className="mt-8">
                <button className="bg-blue-500 text-white px-4 py-2 rounded">Get Started</button>
            </div>
        </div>
    );
};

export default Home;