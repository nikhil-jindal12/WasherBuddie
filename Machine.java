import java.time.LocalDateTime;

public class Machine {
    public static void main(String[] args) {
    }

    private String currentState;
    private LocalDateTime startTime;
    private LocalDateTime endTime;
    private int functionalityState;

    // Getters/Setters
    public String getCurrentState() {
        return currentState;
    }
    public void setCurrentState(String currentState) {
        this.currentState = currentState;
    }

    public LocalDateTime getStartTime() {
        return startTime;
    }
    public void setStartTime(LocalDateTime startTime) {
        this.startTime = startTime;
    }

    public LocalDateTime getEndTime() {
        return endTime;
    }
    public void setEndTime(LocalDateTime endTime) {
        this.endTime = endTime;
    }

    public int getFunctionalityState() {
        return functionalityState;
    }
    public void setFunctionalityState(int functionalityState) {
        this.functionalityState = functionalityState;
    }
}