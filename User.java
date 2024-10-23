public class User {
    public static void main(String[] args) {
    }

    private String userName;
    private int userNumber;
    private String userEmail;
    private boolean notificationPreference;
    // Future admin implementation
    private boolean isAdmin = false;

    // Getters/Setters
    public String getUserName() {
        return userName;
    }
    public void setUserName(String userName) {
        this.userName = userName;
    }
    
    public int getUserNumber() {
        return userNumber;
    }
    public void setUserNumber(int userNumber) {
        this.userNumber = userNumber;
    }

    public String getUserEmail() {
        return userEmail;
    }
    public void setUserEmail(String userEmail) {
        this.userEmail = userEmail;
    }

    public boolean getNotificationPreference() {
        return notificationPreference;
    }
    public void setNotificationPreference(boolean notificationPreference) {
        this.notificationPreference = notificationPreference;
    }

    public boolean getAdminPrivelage() {
        return isAdmin;
    }
}
