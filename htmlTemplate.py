css = '''
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* Global Styles */
.stApp {
    font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
}

/* Main content area */
.main .block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    margin: 1rem;
}

/* Header styling */
h1 {
    color: white !important;
    text-align: center;
    font-weight: 700;
    font-size: 2.5rem;
    margin-bottom: 2rem;
    text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.3);
    background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradientShift 3s ease infinite;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Chat message container */
.chat-message {
    padding: 1.5rem;
    border-radius: 20px;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: flex-start;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    animation: slideIn 0.5s ease-out;
    position: relative;
    overflow: hidden;
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* User message styling */
.chat-message.user {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    margin-left: 10%;
    border-bottom-right-radius: 5px;
}

.chat-message.user::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(45deg, rgba(255, 255, 255, 0.1), transparent);
    pointer-events: none;
}

/* Bot message styling */
.chat-message.bot {
    background: linear-gradient(135deg, #2d3748 0%, #4a5568 100%);
    margin-right: 10%;
    border-bottom-left-radius: 5px;
}

.chat-message.bot::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(45deg, rgba(255, 255, 255, 0.05), transparent);
    pointer-events: none;
}

/* Avatar styling */
.chat-message .avatar {
    width: 60px;
    height: 60px;
    margin-right: 1rem;
    flex-shrink: 0;
}

.chat-message .avatar img {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    object-fit: cover;
    border: 3px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    transition: transform 0.3s ease;
}

.chat-message .avatar img:hover {
    transform: scale(1.1);
}

/* Message text styling */
.chat-message .message {
    flex: 1;
    color: #ffffff;
    font-size: 1rem;
    line-height: 1.6;
    font-weight: 400;
    position: relative;
    z-index: 1;
}

/* Sidebar styling */
.css-1d391kg {
    background: rgba(255, 255, 255, 0.1) !important;
    backdrop-filter: blur(15px) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.2) !important;
}

/* Input field styling */
.stTextInput > div > div > input {
    background: rgba(255, 255, 255, 0.1) !important;
    border: 2px solid rgba(255, 255, 255, 0.2) !important;
    border-radius: 15px !important;
    color: white !important;
    font-size: 1rem !important;
    padding: 0.75rem 1rem !important;
    backdrop-filter: blur(10px) !important;
    transition: all 0.3s ease !important;
}

.stTextInput > div > div > input:focus {
    border-color: #4ecdc4 !important;
    box-shadow: 0 0 20px rgba(78, 205, 196, 0.3) !important;
    transform: translateY(-2px) !important;
}

.stTextInput > div > div > input::placeholder {
    color: rgba(255, 255, 255, 0.6) !important;
}

/* Button styling */
.stButton > button {
    background: linear-gradient(135deg, #4ecdc4 0%, #44a08d 100%) !important;
    border: none !important;
    border-radius: 15px !important;
    color: white !important;
    font-weight: 600 !important;
    padding: 0.75rem 2rem !important;
    font-size: 1rem !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(78, 205, 196, 0.3) !important;
}

.stButton > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 8px 25px rgba(78, 205, 196, 0.4) !important;
    background: linear-gradient(135deg, #44a08d 0%, #4ecdc4 100%) !important;
}

/* File uploader styling */
.stFileUploader > div {
    background: rgba(255, 255, 255, 0.1) !important;
    border: 2px dashed rgba(255, 255, 255, 0.3) !important;
    border-radius: 15px !important;
    padding: 2rem !important;
    transition: all 0.3s ease !important;
}

.stFileUploader > div:hover {
    border-color: #4ecdc4 !important;
    background: rgba(78, 205, 196, 0.1) !important;
}

/* Subheader styling */
.css-10trblm {
    color: white !important;
    font-weight: 600 !important;
    font-size: 1.2rem !important;
    margin-bottom: 1rem !important;
}

/* Success/Error message styling */
.stSuccess, .stError, .stInfo {
    border-radius: 15px !important;
    border: none !important;
    backdrop-filter: blur(10px) !important;
}

.stSuccess {
    background: rgba(72, 187, 120, 0.2) !important;
    border-left: 4px solid #48bb78 !important;
}

.stError {
    background: rgba(245, 101, 101, 0.2) !important;
    border-left: 4px solid #f56565 !important;
}

.stInfo {
    background: rgba(66, 153, 225, 0.2) !important;
    border-left: 4px solid #4299e1 !important;
}

/* Spinner styling */
.stSpinner > div {
    border-top-color: #4ecdc4 !important;
}

/* Scrollbar styling */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(135deg, #4ecdc4, #44a08d);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(135deg, #44a08d, #4ecdc4);
}

/* Mobile responsiveness */
@media (max-width: 768px) {
    .chat-message {
        margin-left: 5% !important;
        margin-right: 5% !important;
        padding: 1rem;
    }
    
    .chat-message .avatar {
        width: 50px;
        height: 50px;
    }
    
    .chat-message .avatar img {
        width: 50px;
        height: 50px;
    }
    
    h1 {
        font-size: 2rem !important;
    }
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://img.icons8.com/fluency/48/chatbot.png" alt="AI Assistant">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://img.icons8.com/fluency/48/user-male-circle.png" alt="User">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''