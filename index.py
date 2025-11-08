<!-- templates/dashboard.html -->
{% extends "base.html" %}

{% block title %}Dashboard - Lakeview Comms CAD{% endblock %}

{% block content %}
<div class="app-container">
    <header>
        <div class="logo-container">
            <img src="https://ik.imagekit.io/seqcqjmzq/e595f6f1-e9e2-44a1-8b97-0c5afc307593.png?updatedAt=1756007991242" alt="Lakeview Comms CAD" class="logo">
            <div class="title">Lakeview Comms CAD</div>
        </div>
        <div class="user-info">
            <div class="status-indicator"></div>
            <div class="user-details">
                <div class="user-id">{{ user.discord_id }}</div>
                <div class="shift-time">Shift: {{ shift_duration }}</div>
            </div>
            <a href="{{ url_for('logout') }}" class="sign-out-btn">
                <i class="fas fa-sign-out-alt"></i> Sign Out
            </a>
        </div>
    </header>

    <div class="main-content">
        <!-- Left Panel: Call List -->
        <div class="panel">
            <div class="panel-header">
                <div class="panel-title">
                    <i class="fas fa-list"></i>
                    Incident Queue
                </div>
                <div class="panel-actions">
                    <button class="btn" id="new-call-btn">
                        <i class="fas fa-plus"></i> New Call
                    </button>
                </div>
            </div>
            <div class="call-list" id="call-list">
                <div class="empty-state">
                    <div class="empty-icon">
                        <i class="fas fa-clipboard-list"></i>
                    </div>
                    <p>No active incidents</p>
                    <p class="text-sm">Create a new call to get started</p>
                </div>
            </div>
        </div>

        <!-- Center Panel: Active Incident -->
        <div class="panel">
            <div class="active-incident">
                <div class="incident-header" id="active-incident-header">
                    <div class="empty-state">
                        <div class="empty-icon">
                            <i class="fas fa-binoculars"></i>
                        </div>
                        <p>No incident selected</p>
                        <p class="text-sm">Select an incident from the queue to view details</p>
                    </div>
                </div>

                <div class="narrative-container">
                    <div class="narrative-title">
                        <i class="fas fa-scroll"></i>
                        Incident Narrative
                    </div>
                    <div class="narrative-log" id="narrative-log">
                        <!-- Narrative entries will be added here -->
                    </div>
                    <div class="narrative-input">
                        <input type="text" id="narrative-input" placeholder="Add narrative entry..." disabled>
                        <button id="add-narrative" disabled>
                            <i class="fas fa-paper-plane"></i>
                        </button>
                    </div>
                </div>

                <div class="assigned-units">
                    <div class="units-title">
                        <i class="fas fa-users"></i>
                        Assigned Units
                    </div>
                    <div class="unit-tags" id="assigned-units">
                        <!-- Assigned units will be added here -->
                    </div>
                </div>

                <div class="unit-assignment">
                    <div class="assignment-title">
                        <i class="fas fa-user-plus"></i>
                        Assign Units
                    </div>
                    <div class="unit-search">
                        <input type="text" id="unit-search" placeholder="Search for units...">
                        <div class="search-results" id="search-results"></div>
                    </div>
                    <div class="custom-select" id="unit-select">
                        <div class="custom-select-header">
                            <span>Select a unit to assign</span>
                            <i class="fas fa-chevron-down"></i>
                        </div>
                        <div class="custom-select-options" id="unit-options">
                            <!-- Unit options will be added here -->
                        </div>
                    </div>
                    <button class="assign-btn" id="assign-btn">
                        <i class="fas fa-plus"></i> Assign Unit
                    </button>
                </div>

                <div class="panel-actions mt-15">
                    <button class="btn priority-btn" id="priority-btn">
                        <i class="fas fa-exclamation-triangle"></i> Priority Situation
                    </button>
                </div>
            </div>
        </div>

        <!-- Right Panel: Unit List -->
        <div class="panel">
            <div class="panel-header">
                <div class="panel-title">
                    <i class="fas fa-car"></i>
                    Unit Status Board
                </div>
                <div class="panel-actions">
                    <button class="btn" id="add-unit-btn">
                        <i class="fas fa-plus"></i> Add Unit
                    </button>
                </div>
            </div>
            <div class="unit-list" id="unit-list">
                <!-- Units will be added here dynamically -->
                <div class="empty-state">
                    <div class="empty-icon">
                        <i class="fas fa-car"></i>
                    </div>
                    <p>No units available</p>
                    <p class="text-sm">Add units to the status board</p>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Tools Button -->
<button class="tools-btn" id="tools-btn">
    <i class="fas fa-tools"></i>
</button>

<!-- Tools Panel -->
<div class="tools-panel" id="tools-panel">
    <div class="tools-header">
        <div class="tools-title">Dispatcher Tools</div>
        <button class="close-tools">&times;</button>
    </div>
    <div class="tools-options">
        <div class="tool-option" data-tool="signal">
            <i class="fas fa-broadcast-tower"></i>
            <div>
                <div class="text-sm">Signal Activation</div>
                <div class="text-xs">Activate emergency signals</div>
            </div>
        </div>
        <div class="tool-option" data-tool="supervisor">
            <i class="fas fa-user-shield"></i>
            <div>
                <div class="text-sm">Supervisor Request</div>
                <div class="text-xs">Request supervisor assistance</div>
            </div>
        </div>
        <div class="tool-option" data-tool="guide">
            <i class="fas fa-book-medical"></i>
            <div>
                <div class="text-sm">911 Call Guide</div>
                <div class="text-xs">Emergency response protocols</div>
            </div>
        </div>
        <div class="tool-option" data-tool="doc">
            <i class="fas fa-file-alt"></i>
            <div>
                <div class="text-sm">Documentation</div>
                <div class="text-xs">Complete system documentation</div>
            </div>
        </div>
    </div>
</div>

<!-- Active Alerts Section -->
<div class="active-alerts" id="active-alerts">
    <!-- Priority and Signal alerts will appear here -->
</div>

<!-- Beta Badge -->
<div class="beta-badge">BETA • Under Development & Testing</div>

<!-- LKVC Branding -->
<div class="lkvc-brand">
    <img src="https://ik.imagekit.io/tycncf0zq0/Lakeview%20City%20Roleplay.png?updatedAt=1762564831685" alt="LKVC" class="lkvc-logo">
    <span>Lakeview City Roleplay</span>
</div>

<!-- Include all modals from the original HTML -->
{% include 'modals.html' %}
{% endblock %}

{% block scripts %}
<script>
    // Initialize the application with user data
    const userData = {{ user | tojson }};
    const shiftDuration = "{{ shift_duration }}";
    
    // Initialize the CAD application
    $(document).ready(function() {
        CADSystem.init(userData, shiftDuration);
    });
</script>
{% endblock %}
