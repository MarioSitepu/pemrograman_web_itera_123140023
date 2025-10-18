document.addEventListener('DOMContentLoaded', function() {
    // Initialize variables
    let tasks = [];
    let currentEditId = null;
    
    // DOM Elements
    const taskForm = document.getElementById('taskForm');
    const editTaskForm = document.getElementById('editTaskForm');
    const taskContainer = document.getElementById('taskContainer');
    const statusFilter = document.getElementById('statusFilter');
    const courseFilter = document.getElementById('courseFilter');
    const searchTask = document.getElementById('searchTask');
    const editModal = document.getElementById('editModal');
    const closeModal = document.getElementById('closeModal');
    const successMessage = document.getElementById('successMessage');
    const loadingSpinner = document.getElementById('loadingSpinner');
    
    // Show loading spinner
    function showLoading() {
        loadingSpinner.style.display = 'block';
        taskContainer.style.display = 'none';
    }
    
    // Hide loading spinner
    function hideLoading() {
        setTimeout(() => {
            loadingSpinner.style.display = 'none';
            taskContainer.style.display = 'block';
        }, 500);
    }
    
    // Load tasks from localStorage
    function loadTasks() {
        showLoading();
        const storedTasks = localStorage.getItem('tasks');
        if (storedTasks) {
            tasks = JSON.parse(storedTasks);
            updateCourseFilter();
            renderTasks();
            updateStats();
        }
        hideLoading();
    }
    
    // Save tasks to localStorage
    function saveTasks() {
        showLoading();
        localStorage.setItem('tasks', JSON.stringify(tasks));
        updateCourseFilter();
        renderTasks();
        updateStats();
        hideLoading();
    }
    
    // Update course filter options
    function updateCourseFilter() {
        const courses = [...new Set(tasks.map(task => task.course))];
        courseFilter.innerHTML = '<option value="all">Semua Mata Kuliah</option>';
        
        courses.forEach(course => {
            const option = document.createElement('option');
            option.value = course;
            option.textContent = course;
            courseFilter.appendChild(option);
        });
    }
    
    // Generate unique ID
    function generateId() {
        return Date.now().toString(36) + Math.random().toString(36).substr(2);
    }
    
    // Format date
    function formatDate(dateString) {
        const options = { year: 'numeric', month: 'long', day: 'numeric' };
        return new Date(dateString).toLocaleDateString('id-ID', options);
    }
    
    // Check if date is overdue
    function isOverdue(dateString) {
        const today = new Date();
        today.setHours(0, 0, 0, 0);
        const deadline = new Date(dateString);
        return deadline < today;
    }
    
    // Show success message
    function showSuccessMessage(message) {
        successMessage.innerHTML = `<i class="fas fa-check-circle"></i> ${message}`;
        successMessage.style.display = 'block';
        setTimeout(() => {
            successMessage.style.display = 'none';
        }, 3000);
    }
    
    // Validate form
    function validateForm(taskName, courseName, taskDeadline, prefix = '') {
        let isValid = true;
        
        // Reset error messages
        document.getElementById(prefix + 'taskNameError').style.display = 'none';
        document.getElementById(prefix + 'courseNameError').style.display = 'none';
        document.getElementById(prefix + 'taskDeadlineError').style.display = 'none';
        
        // Validate task name
        if (!taskName.trim()) {
            document.getElementById(prefix + 'taskNameError').style.display = 'block';
            isValid = false;
        }
        
        // Validate course name
        if (!courseName.trim()) {
            document.getElementById(prefix + 'courseNameError').style.display = 'block';
            isValid = false;
        }
        
        // Validate deadline
        if (!taskDeadline) {
            document.getElementById(prefix + 'taskDeadlineError').style.display = 'block';
            isValid = false;
        }
        
        return isValid;
    }
    
    // Add new task
    function addTask(e) {
        e.preventDefault();
        
        const taskName = document.getElementById('taskName').value;
        const courseName = document.getElementById('courseName').value;
        const taskDeadline = document.getElementById('taskDeadline').value;
        
        if (!validateForm(taskName, courseName, taskDeadline)) {
            return;
        }
        
        const newTask = {
            id: generateId(),
            name: taskName,
            course: courseName,
            deadline: taskDeadline,
            completed: false,
            createdAt: new Date().toISOString()
        };
        
        tasks.push(newTask);
        saveTasks();
        
        // Reset form
        taskForm.reset();
        
        showSuccessMessage('Tugas berhasil ditambahkan!');
    }
    
    // Edit task
    function editTask(id) {
        const task = tasks.find(t => t.id === id);
        if (!task) return;
        
        currentEditId = id;
        document.getElementById('editTaskName').value = task.name;
        document.getElementById('editCourseName').value = task.course;
        document.getElementById('editTaskDeadline').value = task.deadline;
        
        editModal.style.display = 'flex';
    }
    
    // Update task
    function updateTask(e) {
        e.preventDefault();
        
        const taskName = document.getElementById('editTaskName').value;
        const courseName = document.getElementById('editCourseName').value;
        const taskDeadline = document.getElementById('editTaskDeadline').value;
        
        if (!validateForm(taskName, courseName, taskDeadline, 'edit')) {
            return;
        }
        
        const taskIndex = tasks.findIndex(t => t.id === currentEditId);
        if (taskIndex !== -1) {
            tasks[taskIndex] = {
                ...tasks[taskIndex],
                name: taskName,
                course: courseName,
                deadline: taskDeadline
            };
            
            saveTasks();
            editModal.style.display = 'none';
            showSuccessMessage('Tugas berhasil diperbarui!');
        }
    }
    
    // Toggle task completion
    function toggleTask(id) {
        const taskIndex = tasks.findIndex(t => t.id === id);
        if (taskIndex !== -1) {
            tasks[taskIndex].completed = !tasks[taskIndex].completed;
            saveTasks();
            showSuccessMessage(
                tasks[taskIndex].completed ? 'Tugas ditandai selesai!' : 'Tugas ditandai belum selesai!'
            );
        }
    }
    
    // Delete task
    function deleteTask(id) {
        if (confirm('Apakah Anda yakin ingin menghapus tugas ini?')) {
            tasks = tasks.filter(t => t.id !== id);
            saveTasks();
            showSuccessMessage('Tugas berhasil dihapus!');
        }
    }
    
    // Filter tasks
    function filterTasks() {
        const statusValue = statusFilter.value;
        const courseValue = courseFilter.value;
        const searchValue = searchTask.value.toLowerCase();
        
        let filteredTasks = tasks;
        
        // Filter by status
        if (statusValue !== 'all') {
            filteredTasks = filteredTasks.filter(task => 
                statusValue === 'completed' ? task.completed : !task.completed
            );
        }
        
        // Filter by course
        if (courseValue !== 'all') {
            filteredTasks = filteredTasks.filter(task => task.course === courseValue);
        }
        
        // Filter by search term
        if (searchValue) {
            filteredTasks = filteredTasks.filter(task => 
                task.name.toLowerCase().includes(searchValue)
            );
        }
        
        return filteredTasks;
    }
    
    // Animate number counting
    function animateValue(id, start, end, duration) {
        const obj = document.getElementById(id);
        const range = end - start;
        const minTimer = 50;
        let stepTime = Math.abs(Math.floor(duration / range));
        stepTime = Math.max(stepTime, minTimer);
        const startTime = new Date().getTime();
        const endTime = startTime + duration;
        
        function run() {
            const now = new Date().getTime();
            const remaining = Math.max((endTime - now) / duration, 0);
            const value = Math.round(end - (remaining * range));
            obj.innerHTML = value;
            if (value < end) {
                requestAnimationFrame(run);
            }
        }
        
        requestAnimationFrame(run);
    }
    
    // Render tasks
    function renderTasks() {
        const filteredTasks = filterTasks();
        
        if (filteredTasks.length === 0) {
            taskContainer.innerHTML = `
                <div class="empty-state">
                    <i class="fas fa-satellite-dish"></i>
                    <p>Tidak ada tugas yang ditemukan.</p>
                </div>
            `;
            return;
        }
        
        // Sort tasks by deadline and completion status
        const sortedTasks = [...filteredTasks].sort((a, b) => {
            // Sort by completion status first (incomplete first)
            if (a.completed !== b.completed) {
                return a.completed ? 1 : -1;
            }
            // Then sort by deadline (earliest first)
            return new Date(a.deadline) - new Date(b.deadline);
        });
        
        taskContainer.innerHTML = '';
        
        sortedTasks.forEach((task, index) => {
            setTimeout(() => {
                const taskElement = document.createElement('div');
                taskElement.className = `task-item ${task.completed ? 'completed' : ''}`;
                
                const overdue = !task.completed && isOverdue(task.deadline);
                
                taskElement.innerHTML = `
                    <div style="display: flex; align-items: center;">
                        <input type="checkbox" class="task-checkbox" ${task.completed ? 'checked' : ''} 
                            onchange="toggleTask('${task.id}')">
                        <div class="task-info">
                            <h3>${task.name} ${overdue ? '<span style="color: var(--accent-color);">(TERLAMBAT)</span>' : ''}</h3>
                            <p><i class="fas fa-book"></i> ${task.course}</p>
                            <p><i class="fas fa-calendar"></i> ${formatDate(task.deadline)}</p>
                        </div>
                    </div>
                    <div class="task-actions">
                        <button class="btn btn-sm btn-warning" onclick="editTask('${task.id}')">
                            <i class="fas fa-edit"></i>
                        </button>
                        <button class="btn btn-sm btn-danger" onclick="deleteTask('${task.id}')">
                            <i class="fas fa-trash"></i>
                        </button>
                    </div>
                `;
                
                taskContainer.appendChild(taskElement);
            }, index * 100);
        });
    }
    
    // Update statistics
    function updateStats() {
        const totalTasks = tasks.length;
        const completedTasks = tasks.filter(task => task.completed).length;
        const pendingTasks = totalTasks - completedTasks;
        
        // Animate the count
        animateValue('totalTasks', 0, totalTasks, 1000);
        animateValue('completedTasks', 0, completedTasks, 1000);
        animateValue('pendingTasks', 0, pendingTasks, 1000);
    }
    
    // Event listeners
    taskForm.addEventListener('submit', addTask);
    editTaskForm.addEventListener('submit', updateTask);
    statusFilter.addEventListener('change', renderTasks);
    courseFilter.addEventListener('change', renderTasks);
    searchTask.addEventListener('input', renderTasks);
    
    closeModal.addEventListener('click', () => {
        editModal.style.display = 'none';
    });
    
    window.addEventListener('click', (e) => {
        if (e.target === editModal) {
            editModal.style.display = 'none';
        }
    });
    
    // Make functions global
    window.toggleTask = toggleTask;
    window.editTask = editTask;
    window.deleteTask = deleteTask;
    
    // Initialize app
    loadTasks();
});