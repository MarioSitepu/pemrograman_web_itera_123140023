document.addEventListener('DOMContentLoaded', function() {
    // Class untuk mengelola tugas
    class TaskManager {
        constructor() {
            this.tasks = [];
            this.currentEditId = null;
            this.init();
        }
        
        // Inisialisasi aplikasi
        init = () => {
            this.loadTasks();
            this.setupEventListeners();
            this.updateStats();
        }
        
        // Setup event listeners
        setupEventListeners = () => {
            document.getElementById('taskForm').addEventListener('submit', this.handleAddTask);
            document.getElementById('editTaskForm').addEventListener('submit', this.handleUpdateTask);
            document.getElementById('statusFilter').addEventListener('change', this.renderTasks);
            document.getElementById('courseFilter').addEventListener('change', this.renderTasks);
            document.getElementById('searchTask').addEventListener('input', this.renderTasks);
            document.getElementById('closeModal').addEventListener('click', this.closeEditModal);
            
            window.addEventListener('click', (e) => {
                if (e.target === document.getElementById('editModal')) {
                    this.closeEditModal();
                }
            });
        }
        
        // Memuat tugas dari localStorage
        loadTasks = async () => {
            this.showLoading();
            
            // Simulasi async operation
            await new Promise(resolve => setTimeout(resolve, 500));
            
            const storedTasks = localStorage.getItem('tasks');
            if (storedTasks) {
                this.tasks = JSON.parse(storedTasks);
                this.updateCourseFilter();
                this.renderTasks();
                this.updateStats();
            }
            
            this.hideLoading();
        }
        
        // Menyimpan tugas ke localStorage
        saveTasks = async () => {
            this.showLoading();
            
            // Simulasi async operation
            await new Promise(resolve => setTimeout(resolve, 500));
            
            localStorage.setItem('tasks', JSON.stringify(this.tasks));
            this.updateCourseFilter();
            this.renderTasks();
            this.updateStats();
            
            this.hideLoading();
        }
        
        // Menampilkan loading spinner
        showLoading = () => {
            document.getElementById('loadingSpinner').style.display = 'block';
            document.getElementById('taskContainer').style.display = 'none';
        }
        
        // Menyembunyikan loading spinner
        hideLoading = () => {
            setTimeout(() => {
                document.getElementById('loadingSpinner').style.display = 'none';
                document.getElementById('taskContainer').style.display = 'block';
            }, 500);
        }
        
        // Memperbarui opsi filter mata kuliah
        updateCourseFilter = () => {
            const courses = [...new Set(this.tasks.map(task => task.course))];
            const courseFilter = document.getElementById('courseFilter');
            
            courseFilter.innerHTML = '<option value="all">Semua Mata Kuliah</option>';
            
            courses.forEach(course => {
                const option = document.createElement('option');
                option.value = course;
                option.textContent = course;
                courseFilter.appendChild(option);
            });
        }
        
        // Menghasilkan ID unik
        generateId = () => {
            return Date.now().toString(36) + Math.random().toString(36).substr(2);
        }
        
        // Format tanggal
        formatDate = (dateString) => {
            const options = { year: 'numeric', month: 'long', day: 'numeric' };
            return new Date(dateString).toLocaleDateString('id-ID', options);
        }
        
        // Mengecek apakah tanggal sudah lewat
        isOverdue = (dateString) => {
            const today = new Date();
            today.setHours(0, 0, 0, 0);
            const deadline = new Date(dateString);
            return deadline < today;
        }
        
        // Menampilkan pesan sukses
        showSuccessMessage = (message) => {
            const successMessage = document.getElementById('successMessage');
            successMessage.innerHTML = `<i class="fas fa-check-circle"></i> ${message}`;
            successMessage.style.display = 'block';
            
            setTimeout(() => {
                successMessage.style.display = 'none';
            }, 3000);
        }
        
        // Validasi form
        validateForm = (taskName, courseName, taskDeadline, prefix = '') => {
            let isValid = true;
            
            // Reset pesan error
            document.getElementById(`${prefix}taskNameError`).style.display = 'none';
            document.getElementById(`${prefix}courseNameError`).style.display = 'none';
            document.getElementById(`${prefix}taskDeadlineError`).style.display = 'none';
            
            // Validasi nama tugas
            if (!taskName.trim()) {
                document.getElementById(`${prefix}taskNameError`).style.display = 'block';
                isValid = false;
            }
            
            // Validasi nama mata kuliah
            if (!courseName.trim()) {
                document.getElementById(`${prefix}courseNameError`).style.display = 'block';
                isValid = false;
            }
            
            // Validasi deadline
            if (!taskDeadline) {
                document.getElementById(`${prefix}taskDeadlineError`).style.display = 'block';
                isValid = false;
            }
            
            return isValid;
        }
        
        // Menangani penambahan tugas baru
        handleAddTask = async (e) => {
            e.preventDefault();
            
            const taskName = document.getElementById('taskName').value;
            const courseName = document.getElementById('courseName').value;
            const taskDeadline = document.getElementById('taskDeadline').value;
            
            if (!this.validateForm(taskName, courseName, taskDeadline)) {
                return;
            }
            
            const newTask = {
                id: this.generateId(),
                name: taskName,
                course: courseName,
                deadline: taskDeadline,
                completed: false,
                createdAt: new Date().toISOString()
            };
            
            this.tasks.push(newTask);
            await this.saveTasks();
            
            // Reset form
            document.getElementById('taskForm').reset();
            
            this.showSuccessMessage('Tugas berhasil ditambahkan!');
        }
        
        // Menangani pembaruan tugas
        handleUpdateTask = async (e) => {
            e.preventDefault();
            
            const taskName = document.getElementById('editTaskName').value;
            const courseName = document.getElementById('editCourseName').value;
            const taskDeadline = document.getElementById('editTaskDeadline').value;
            
            if (!this.validateForm(taskName, courseName, taskDeadline, 'edit')) {
                return;
            }
            
            const taskIndex = this.tasks.findIndex(t => t.id === this.currentEditId);
            if (taskIndex !== -1) {
                this.tasks[taskIndex] = {
                    ...this.tasks[taskIndex],
                    name: taskName,
                    course: courseName,
                    deadline: taskDeadline
                };
                
                await this.saveTasks();
                this.closeEditModal();
                this.showSuccessMessage('Tugas berhasil diperbarui!');
            }
        }
        
        // Membuka modal edit tugas
        openEditModal = (id) => {
            const task = this.tasks.find(t => t.id === id);
            if (!task) return;
            
            this.currentEditId = id;
            document.getElementById('editTaskName').value = task.name;
            document.getElementById('editCourseName').value = task.course;
            document.getElementById('editTaskDeadline').value = task.deadline;
            
            document.getElementById('editModal').style.display = 'flex';
        }
        
        // Menutup modal edit tugas
        closeEditModal = () => {
            document.getElementById('editModal').style.display = 'none';
        }
        
        // Mengubah status penyelesaian tugas
        toggleTaskCompletion = async (id) => {
            const taskIndex = this.tasks.findIndex(t => t.id === id);
            if (taskIndex !== -1) {
                this.tasks[taskIndex].completed = !this.tasks[taskIndex].completed;
                await this.saveTasks();
                this.showSuccessMessage(
                    this.tasks[taskIndex].completed ? 'Tugas ditandai selesai!' : 'Tugas ditandai belum selesai!'
                );
            }
        }
        
        // Menghapus tugas
        deleteTask = async (id) => {
            if (confirm('Apakah Anda yakin ingin menghapus tugas ini?')) {
                this.tasks = this.tasks.filter(t => t.id !== id);
                await this.saveTasks();
                this.showSuccessMessage('Tugas berhasil dihapus!');
            }
        }
        
        // Filter tugas
        filterTasks = () => {
            const statusValue = document.getElementById('statusFilter').value;
            const courseValue = document.getElementById('courseFilter').value;
            const searchValue = document.getElementById('searchTask').value.toLowerCase();
            
            let filteredTasks = this.tasks;
            
            // Filter berdasarkan status
            if (statusValue !== 'all') {
                filteredTasks = filteredTasks.filter(task => 
                    statusValue === 'completed' ? task.completed : !task.completed
                );
            }
            
            // Filter berdasarkan mata kuliah
            if (courseValue !== 'all') {
                filteredTasks = filteredTasks.filter(task => task.course === courseValue);
            }
            
            // Filter berdasarkan pencarian
            if (searchValue) {
                filteredTasks = filteredTasks.filter(task => 
                    task.name.toLowerCase().includes(searchValue)
                );
            }
            
            return filteredTasks;
        }
        
        // Animasi penghitungan angka
        animateValue = (id, start, end, duration) => {
            const obj = document.getElementById(id);
            const range = end - start;
            const minTimer = 50;
            let stepTime = Math.abs(Math.floor(duration / range));
            stepTime = Math.max(stepTime, minTimer);
            const startTime = new Date().getTime();
            const endTime = startTime + duration;
            
            const run = () => {
                const now = new Date().getTime();
                const remaining = Math.max((endTime - now) / duration, 0);
                const value = Math.round(end - (remaining * range));
                obj.innerHTML = value;
                if (value < end) {
                    requestAnimationFrame(run);
                }
            };
            
            requestAnimationFrame(run);
        }
        
        // Render tugas
        renderTasks = () => {
            const filteredTasks = this.filterTasks();
            const taskContainer = document.getElementById('taskContainer');
            
            if (filteredTasks.length === 0) {
                taskContainer.innerHTML = `
                    <div class="empty-state">
                        <i class="fas fa-satellite-dish"></i>
                        <p>Tidak ada tugas yang ditemukan.</p>
                    </div>
                `;
                return;
            }
            
            // Sort tugas berdasarkan deadline dan status penyelesaian
            const sortedTasks = [...filteredTasks].sort((a, b) => {
                // Sort berdasarkan status penyelesaian terlebih dahulu (belum selesai dulu)
                if (a.completed !== b.completed) {
                    return a.completed ? 1 : -1;
                }
                // Kemudian sort berdasarkan deadline (terdekat dulu)
                return new Date(a.deadline) - new Date(b.deadline);
            });
            
            taskContainer.innerHTML = '';
            
            sortedTasks.forEach((task, index) => {
                setTimeout(() => {
                    const taskElement = document.createElement('div');
                    taskElement.className = `task-item ${task.completed ? 'completed' : ''}`;
                    
                    const overdue = !task.completed && this.isOverdue(task.deadline);
                    
                    taskElement.innerHTML = `
                        <div style="display: flex; align-items: center;">
                            <input type="checkbox" class="task-checkbox" ${task.completed ? 'checked' : ''} 
                                onchange="taskManager.toggleTaskCompletion('${task.id}')">
                            <div class="task-info">
                                <h3>${task.name} ${overdue ? '<span style="color: var(--accent-color);">(TERLAMBAT)</span>' : ''}</h3>
                                <p><i class="fas fa-book"></i> ${task.course}</p>
                                <p><i class="fas fa-calendar"></i> ${this.formatDate(task.deadline)}</p>
                            </div>
                        </div>
                        <div class="task-actions">
                            <button class="btn btn-sm btn-warning" onclick="taskManager.openEditModal('${task.id}')">
                                <i class="fas fa-edit"></i>
                            </button>
                            <button class="btn btn-sm btn-danger" onclick="taskManager.deleteTask('${task.id}')">
                                <i class="fas fa-trash"></i>
                            </button>
                        </div>
                    `;
                    
                    taskContainer.appendChild(taskElement);
                }, index * 100);
            });
        }
        
        // Memperbarui statistik
        updateStats = () => {
            const totalTasks = this.tasks.length;
            const completedTasks = this.tasks.filter(task => task.completed).length;
            const pendingTasks = totalTasks - completedTasks;
            
            // Animasi penghitungan
            this.animateValue('totalTasks', 0, totalTasks, 1000);
            this.animateValue('completedTasks', 0, completedTasks, 1000);
            this.animateValue('pendingTasks', 0, pendingTasks, 1000);
        }
    }
    
    // Membuat instance TaskManager dan membuatnya global
    const taskManager = new TaskManager();
    window.taskManager = taskManager;
});