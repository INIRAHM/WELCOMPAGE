import tkinter as tk
from tkinter import messagebox
import json
import os

class InirahApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inirah - Company Portal")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f0f0")
        
        # Center the window on screen
        self.center_window()
        
        # User database file
        self.users_file = "users.json"
        self.load_user_database()
        
        # Show welcome page first
        self.show_welcome_page()
    
    def center_window(self):
        """Center the window on the screen"""
        self.root.update_idletasks()
        width = 500
        height = 600
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def load_user_database(self):
        """Load existing users or create default ones"""
        if os.path.exists(self.users_file):
            with open(self.users_file, 'r') as f:
                self.users = json.load(f)
        else:
            # Create default users for demo
            self.users = {
                "admin": {"password": "admin123", "name": "Administrator", "role": "Admin"},
                "john": {"password": "john123", "name": "John Doe", "role": "Employee"},
                "jane": {"password": "jane123", "name": "Jane Smith", "role": "Manager"}
            }
            self.save_users()
    
    def save_users(self):
        """Save users to JSON file"""
        with open(self.users_file, 'w') as f:
            json.dump(self.users, f, indent=4)
    
    def show_welcome_page(self):
        """Display the welcome page"""
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Welcome Page Design
        welcome_frame = tk.Frame(self.root, bg="#f0f0f0")
        welcome_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Company Logo/Name
        company_label = tk.Label(welcome_frame, text="INIRAH", 
                                 font=("Arial", 48, "bold"), 
                                 bg="#f0f0f0", fg="#2c3e50")
        company_label.pack(pady=(50, 10))
        
        # Tagline
        tagline = tk.Label(welcome_frame, text="Innovating Tomorrow's Solutions Today", 
                          font=("Arial", 12, "italic"), 
                          bg="#f0f0f0", fg="#7f8c8d")
        tagline.pack(pady=(0, 50))
        
        # Welcome Message
        welcome_text = tk.Label(welcome_frame, text="Welcome to Inirah Portal", 
                               font=("Arial", 20, "bold"), 
                               bg="#f0f0f0", fg="#34495e")
        welcome_text.pack(pady=20)
        
        # Description
        description = tk.Label(welcome_frame, 
                              text="Your trusted partner in digital transformation.\n\n"
                                   "Please login to access your dashboard and manage your tasks.\n\n"
                                   "Demo credentials:\n"
                                   "Username: admin | Password: admin123\n"
                                   "Username: john | Password: john123\n"
                                   "Username: jane | Password: jane123",
                              font=("Arial", 10), 
                              bg="#f0f0f0", fg="#7f8c8d", 
                              justify="center")
        description.pack(pady=30)
        
        # Login Button
        login_btn = tk.Button(welcome_frame, text="Login to Your Account", 
                             command=self.show_login_page,
                             font=("Arial", 14, "bold"),
                             bg="#3498db", fg="white", 
                             padx=30, pady=10,
                             relief="flat", cursor="hand2")
        login_btn.pack(pady=20)
        
        # Hover effect for button
        def on_enter(e):
            login_btn['background'] = "#2980b9"
        
        def on_leave(e):
            login_btn['background'] = "#3498db"
        
        login_btn.bind("<Enter>", on_enter)
        login_btn.bind("<Leave>", on_leave)
        
        # Footer
        footer = tk.Label(welcome_frame, text="© 2024 Inirah. All rights reserved.", 
                         font=("Arial", 8), 
                         bg="#f0f0f0", fg="#95a5a6")
        footer.pack(side="bottom", pady=20)
    
    def show_login_page(self):
        """Display the login page"""
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Login Page Design
        login_frame = tk.Frame(self.root, bg="#f0f0f0")
        login_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Back button to welcome page
        back_btn = tk.Button(login_frame, text="← Back", 
                            command=self.show_welcome_page,
                            font=("Arial", 10),
                            bg="#95a5a6", fg="white",
                            relief="flat", cursor="hand2",
                            padx=10, pady=5)
        back_btn.pack(anchor="nw", pady=(0, 20))
        
        # Company Logo
        company_label = tk.Label(login_frame, text="INIRAH", 
                                 font=("Arial", 32, "bold"), 
                                 bg="#f0f0f0", fg="#2c3e50")
        company_label.pack(pady=(20, 30))
        
        # Login Card
        login_card = tk.Frame(login_frame, bg="white", relief="solid", bd=1)
        login_card.pack(pady=20, padx=30, fill="both", expand=True)
        
        # Login Title
        login_title = tk.Label(login_card, text="Login to Your Account", 
                               font=("Arial", 18, "bold"), 
                               bg="white", fg="#34495e")
        login_title.pack(pady=(30, 20))
        
        # Username
        username_label = tk.Label(login_card, text="Username:", 
                                  font=("Arial", 12), 
                                  bg="white", fg="#2c3e50")
        username_label.pack(anchor="w", padx=40, pady=(20, 5))
        
        self.username_entry = tk.Entry(login_card, font=("Arial", 12), 
                                       relief="solid", bd=1)
        self.username_entry.pack(fill="x", padx=40, pady=(0, 15))
        
        # Password
        password_label = tk.Label(login_card, text="Password:", 
                                  font=("Arial", 12), 
                                  bg="white", fg="#2c3e50")
        password_label.pack(anchor="w", padx=40, pady=(10, 5))
        
        self.password_entry = tk.Entry(login_card, font=("Arial", 12), 
                                       relief="solid", bd=1, show="•")
        self.password_entry.pack(fill="x", padx=40, pady=(0, 20))
        
        # Login Button
        login_btn = tk.Button(login_card, text="Login", 
                             command=self.authenticate_user,
                             font=("Arial", 14, "bold"),
                             bg="#27ae60", fg="white",
                             padx=30, pady=8,
                             relief="flat", cursor="hand2")
        login_btn.pack(pady=20)
        
        # Hover effect for login button
        def on_enter(e):
            login_btn['background'] = "#229954"
        
        def on_leave(e):
            login_btn['background'] = "#27ae60"
        
        login_btn.bind("<Enter>", on_enter)
        login_btn.bind("<Leave>", on_leave)
        
        # Register link
        register_link = tk.Button(login_card, text="Don't have an account? Register here", 
                                 command=self.show_register_page,
                                 font=("Arial", 9), 
                                 bg="white", fg="#3498db",
                                 relief="flat", cursor="hand2")
        register_link.pack(pady=(0, 30))
        
        # Bind Enter key to login
        self.username_entry.bind("<Return>", lambda e: self.authenticate_user())
        self.password_entry.bind("<Return>", lambda e: self.authenticate_user())
    
    def show_register_page(self):
        """Display registration page for new users"""
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Registration Page Design
        reg_frame = tk.Frame(self.root, bg="#f0f0f0")
        reg_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Back button
        back_btn = tk.Button(reg_frame, text="← Back to Login", 
                            command=self.show_login_page,
                            font=("Arial", 10),
                            bg="#95a5a6", fg="white",
                            relief="flat", cursor="hand2",
                            padx=10, pady=5)
        back_btn.pack(anchor="nw", pady=(0, 20))
        
        # Registration Card
        reg_card = tk.Frame(reg_frame, bg="white", relief="solid", bd=1)
        reg_card.pack(pady=20, padx=30, fill="both", expand=True)
        
        # Registration Title
        reg_title = tk.Label(reg_card, text="Create New Account", 
                            font=("Arial", 18, "bold"), 
                            bg="white", fg="#34495e")
        reg_title.pack(pady=(30, 20))
        
        # Full Name
        name_label = tk.Label(reg_card, text="Full Name:", 
                             font=("Arial", 12), 
                             bg="white", fg="#2c3e50")
        name_label.pack(anchor="w", padx=40, pady=(20, 5))
        
        self.reg_name_entry = tk.Entry(reg_card, font=("Arial", 12), 
                                       relief="solid", bd=1)
        self.reg_name_entry.pack(fill="x", padx=40, pady=(0, 15))
        
        # Username
        reg_username_label = tk.Label(reg_card, text="Username:", 
                                     font=("Arial", 12), 
                                     bg="white", fg="#2c3e50")
        reg_username_label.pack(anchor="w", padx=40, pady=(10, 5))
        
        self.reg_username_entry = tk.Entry(reg_card, font=("Arial", 12), 
                                          relief="solid", bd=1)
        self.reg_username_entry.pack(fill="x", padx=40, pady=(0, 15))
        
        # Password
        reg_password_label = tk.Label(reg_card, text="Password:", 
                                     font=("Arial", 12), 
                                     bg="white", fg="#2c3e50")
        reg_password_label.pack(anchor="w", padx=40, pady=(10, 5))
        
        self.reg_password_entry = tk.Entry(reg_card, font=("Arial", 12), 
                                          relief="solid", bd=1, show="•")
        self.reg_password_entry.pack(fill="x", padx=40, pady=(0, 15))
        
        # Confirm Password
        confirm_label = tk.Label(reg_card, text="Confirm Password:", 
                                font=("Arial", 12), 
                                bg="white", fg="#2c3e50")
        confirm_label.pack(anchor="w", padx=40, pady=(10, 5))
        
        self.confirm_entry = tk.Entry(reg_card, font=("Arial", 12), 
                                     relief="solid", bd=1, show="•")
        self.confirm_entry.pack(fill="x", padx=40, pady=(0, 20))
        
        # Register Button
        register_btn = tk.Button(reg_card, text="Register", 
                                command=self.register_user,
                                font=("Arial", 14, "bold"),
                                bg="#e67e22", fg="white",
                                padx=30, pady=8,
                                relief="flat", cursor="hand2")
        register_btn.pack(pady=20)
        
        # Hover effect
        def on_enter(e):
            register_btn['background'] = "#d35400"
        
        def on_leave(e):
            register_btn['background'] = "#e67e22"
        
        register_btn.bind("<Enter>", on_enter)
        register_btn.bind("<Leave>", on_leave)
    
    def register_user(self):
        """Register a new user"""
        name = self.reg_name_entry.get().strip()
        username = self.reg_username_entry.get().strip()
        password = self.reg_password_entry.get()
        confirm = self.confirm_entry.get()
        
        # Validation
        if not name or not username or not password:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        if password != confirm:
            messagebox.showerror("Error", "Passwords do not match!")
            return
        
        if username in self.users:
            messagebox.showerror("Error", "Username already exists! Please choose another.")
            return
        
        # Register new user
        self.users[username] = {
            "password": password,
            "name": name,
            "role": "Employee"
        }
        self.save_users()
        
        messagebox.showinfo("Success", f"Account created successfully!\nWelcome {name}!\nYou can now login.")
        self.show_login_page()
    
    def authenticate_user(self):
        """Authenticate user credentials"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username in self.users and self.users[username]["password"] == password:
            user_info = self.users[username]
            messagebox.showinfo("Login Success", 
                               f"Welcome back, {user_info['name']}!\nRole: {user_info['role']}")
            self.show_dashboard(username, user_info)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")
    
    def show_dashboard(self, username, user_info):
        """Display user dashboard after successful login"""
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Dashboard Page Design
        dashboard_frame = tk.Frame(self.root, bg="#ecf0f1")
        dashboard_frame.pack(expand=True, fill="both")
        
        # Header
        header_frame = tk.Frame(dashboard_frame, bg="#2c3e50", height=100)
        header_frame.pack(fill="x", pady=(0, 20))
        header_frame.pack_propagate(False)
        
        # Company name in header
        company_label = tk.Label(header_frame, text="INIRAH", 
                                font=("Arial", 24, "bold"), 
                                bg="#2c3e50", fg="white")
        company_label.pack(side="left", padx=20, pady=30)
        
        # User info in header
        user_label = tk.Label(header_frame, 
                             text=f"Welcome, {user_info['name']}\nRole: {user_info['role']}", 
                             font=("Arial", 10), 
                             bg="#2c3e50", fg="#ecf0f1")
        user_label.pack(side="right", padx=20, pady=20)
        
        # Content Frame
        content_frame = tk.Frame(dashboard_frame, bg="#ecf0f1")
        content_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Dashboard Title
        dashboard_title = tk.Label(content_frame, text="User Dashboard", 
                                  font=("Arial", 24, "bold"), 
                                  bg="#ecf0f1", fg="#34495e")
        dashboard_title.pack(pady=(0, 30))
        
        # Features based on role
        if user_info['role'] == 'Admin':
            features = [
                "📊 Manage Users",
                "📈 View Analytics",
                "⚙️ System Settings",
                "📋 Reports",
                "👥 Team Management"
            ]
        elif user_info['role'] == 'Manager':
            features = [
                "📊 Team Dashboard",
                "📋 Project Reports",
                "👥 Team Tasks",
                "📈 Performance Metrics"
            ]
        else:
            features = [
                "📝 My Tasks",
                "⏰ Attendance",
                "📅 Calendar",
                "💬 Messages",
                "📄 My Documents"
            ]
        
        # Display features
        for feature in features:
            feature_frame = tk.Frame(content_frame, bg="white", relief="solid", bd=1)
            feature_frame.pack(fill="x", padx=50, pady=10)
            
            feature_label = tk.Label(feature_frame, text=feature, 
                                    font=("Arial", 12), 
                                    bg="white", fg="#2c3e50",
                                    padx=20, pady=15)
            feature_label.pack(anchor="w")
        
        # Logout Button
        logout_btn = tk.Button(content_frame, text="Logout", 
                              command=self.show_welcome_page,
                              font=("Arial", 12, "bold"),
                              bg="#e74c3c", fg="white",
                              padx=20, pady=10,
                              relief="flat", cursor="hand2")
        logout_btn.pack(pady=30)
        
        # Hover effect for logout
        def on_enter(e):
            logout_btn['background'] = "#c0392b"
        
        def on_leave(e):
            logout_btn['background'] = "#e74c3c"
        
        logout_btn.bind("<Enter>", on_enter)
        logout_btn.bind("<Leave>", on_leave)

def main():
    root = tk.Tk()
    app = InirahApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
