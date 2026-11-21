/**
 * BPO COMPANY — Forms Module
 * Demo Form Validation and Frontend-Only Interactive Feedback
 * (No backend transmission, strictly frontend demonstration)
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Business Contact Enquiry Form
  const contactForm = document.getElementById('bpo-contact-form');
  const contactAlert = document.getElementById('contact-form-alert');

  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      let isValid = true;

      // Fields
      const fullName = contactForm.querySelector('[name="full_name"]');
      const email = contactForm.querySelector('[name="email"]');
      const company = contactForm.querySelector('[name="company"]');
      const phone = contactForm.querySelector('[name="phone"]');
      const service = contactForm.querySelector('[name="service"]');
      const message = contactForm.querySelector('[name="message"]');

      // Helper validation
      const validateInput = (input, condition) => {
        if (!condition) {
          input?.classList.add('is-invalid');
          input?.classList.remove('is-valid');
          isValid = false;
        } else {
          input?.classList.remove('is-invalid');
          input?.classList.add('is-valid');
        }
      };

      if (fullName) validateInput(fullName, fullName.value.trim().length >= 2);
      if (email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        validateInput(email, emailRegex.test(email.value.trim()));
      }
      if (company) validateInput(company, company.value.trim().length >= 2);
      if (phone) {
        const phoneRegex = /^[\d\s+\-()]{7,15}$/;
        validateInput(phone, phoneRegex.test(phone.value.trim()));
      }
      if (service) validateInput(service, service.value !== '');
      if (message) validateInput(message, message.value.trim().length >= 10);

      if (isValid) {
        if (contactAlert) {
          contactAlert.className = 'alert alert-success';
          contactAlert.innerHTML = `
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
              <polyline points="22 4 12 14.01 9 11.01"></polyline>
            </svg>
            <div>
              <strong>Enquiry Received:</strong> Demo enquiry submitted successfully. No information has been transmitted or stored.
            </div>
          `;
          contactAlert.style.display = 'flex';
          contactAlert.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
        contactForm.reset();
        contactForm.querySelectorAll('.is-valid').forEach(el => el.classList.remove('is-valid'));
      }
    });
  }

  // 2. Demo Job Application Form
  const jobForm = document.getElementById('demo-job-application-form');
  const jobAlert = document.getElementById('job-form-alert');
  const resumeInput = document.getElementById('resume-file-input');
  const filePreview = document.getElementById('file-preview-card');
  const fileNameDisplay = document.getElementById('file-name-text');
  const fileSizeDisplay = document.getElementById('file-size-text');
  const clearFileBtn = document.getElementById('clear-file-btn');
  const uploadArea = document.getElementById('file-drop-zone');

  // File Upload Handlers
  if (resumeInput && filePreview) {
    const handleFileSelect = (file) => {
      if (!file) return;

      const validTypes = [
        'application/pdf',
        'application/msword',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
      ];
      const validExtensions = ['.pdf', '.doc', '.docx'];
      const fileExt = '.' + file.name.split('.').pop().toLowerCase();

      if (!validTypes.includes(file.type) && !validExtensions.includes(fileExt)) {
        alert('Invalid file format. Please select a valid PDF, DOC, or DOCX document.');
        resumeInput.value = '';
        return;
      }

      // 5MB limit
      const maxSize = 5 * 1024 * 1024;
      if (file.size > maxSize) {
        alert('File size exceeds 5MB limit. Please select a smaller file.');
        resumeInput.value = '';
        return;
      }

      // Display filename & formatted size
      if (fileNameDisplay) fileNameDisplay.textContent = file.name;
      if (fileSizeDisplay) {
        const sizeFormatted = (file.size / 1024 / 1024).toFixed(2) + ' MB';
        fileSizeDisplay.textContent = sizeFormatted;
      }
      filePreview.classList.add('active');
    };

    resumeInput.addEventListener('change', (e) => {
      const file = e.target.files[0];
      handleFileSelect(file);
    });

    if (clearFileBtn) {
      clearFileBtn.addEventListener('click', (e) => {
        e.preventDefault();
        resumeInput.value = '';
        filePreview.classList.remove('active');
        if (fileNameDisplay) fileNameDisplay.textContent = '';
        if (fileSizeDisplay) fileSizeDisplay.textContent = '';
      });
    }

    // Drag and drop events
    if (uploadArea) {
      ['dragenter', 'dragover'].forEach(eventName => {
        uploadArea.addEventListener(eventName, (e) => {
          e.preventDefault();
          uploadArea.classList.add('dragover');
        });
      });
      ['dragleave', 'drop'].forEach(eventName => {
        uploadArea.addEventListener(eventName, (e) => {
          e.preventDefault();
          uploadArea.classList.remove('dragover');
        });
      });
      uploadArea.addEventListener('drop', (e) => {
        if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
          resumeInput.files = e.dataTransfer.files;
          handleFileSelect(e.dataTransfer.files[0]);
        }
      });
    }
  }

  // Application Submit
  if (jobForm) {
    jobForm.addEventListener('submit', (e) => {
      e.preventDefault();
      let isValid = true;

      const applicantName = jobForm.querySelector('[name="applicant_name"]');
      const applicantEmail = jobForm.querySelector('[name="applicant_email"]');
      const applicantPhone = jobForm.querySelector('[name="applicant_phone"]');
      const applicantLocation = jobForm.querySelector('[name="applicant_location"]');
      const applicantRole = jobForm.querySelector('[name="job_role"]');
      const applicantExp = jobForm.querySelector('[name="experience_level"]');

      const validateInput = (input, condition) => {
        if (!condition) {
          input?.classList.add('is-invalid');
          input?.classList.remove('is-valid');
          isValid = false;
        } else {
          input?.classList.remove('is-invalid');
          input?.classList.add('is-valid');
        }
      };

      if (applicantName) validateInput(applicantName, applicantName.value.trim().length >= 2);
      if (applicantEmail) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        validateInput(applicantEmail, emailRegex.test(applicantEmail.value.trim()));
      }
      if (applicantPhone) {
        const phoneRegex = /^[\d\s+\-()]{7,15}$/;
        validateInput(applicantPhone, phoneRegex.test(applicantPhone.value.trim()));
      }
      if (applicantLocation) validateInput(applicantLocation, applicantLocation.value.trim().length >= 2);
      if (applicantRole) validateInput(applicantRole, applicantRole.value !== '');
      if (applicantExp) validateInput(applicantExp, applicantExp.value !== '');

      if (isValid) {
        if (jobAlert) {
          jobAlert.className = 'alert alert-success';
          jobAlert.innerHTML = `
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
              <polyline points="22 4 12 14.01 9 11.01"></polyline>
            </svg>
            <div>
              <strong>Demo Job Application Submitted:</strong> This is a frontend demonstration. Your submitted information and resume are not delivered to a recruiter or stored on any server.
            </div>
          `;
          jobAlert.style.display = 'flex';
          jobAlert.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
        jobForm.reset();
        if (filePreview) filePreview.classList.remove('active');
        jobForm.querySelectorAll('.is-valid').forEach(el => el.classList.remove('is-valid'));
      }
    });
  }
});
