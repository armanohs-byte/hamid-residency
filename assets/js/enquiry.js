/**
 * HAMID RESIDENCY - TENANT ENQUIRY & VISIT BOOKING LOGIC
 * Direct Owner Connection & WhatsApp Message Generator
 */

// Centralized Contact Settings - Owner can update this one object:
const OWNER_CONFIG = {
  phoneDisplay: "+91 84208 38820",
  phoneRaw: "918420838820", // Owner WhatsApp number (country code + 10 digits without spaces or plus)
  propertyName: "Hamid Residency, Khagrabari, Cooch Behar"
};

document.addEventListener('DOMContentLoaded', () => {
  initEnquiryForm();
  initVisitModal();
  initFloorSelectTriggers();
});

/**
 * Handle Main Enquiry Form Submissions
 */
function initEnquiryForm() {
  const form = document.getElementById('rentalEnquiryForm');
  const whatsappBtn = document.getElementById('sendWhatsappBtn');

  if (!form) return;

  if (whatsappBtn) {
    whatsappBtn.addEventListener('click', (e) => {
      e.preventDefault();
      sendViaWhatsApp(form);
    });
  }

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    handleFormSubmission(form);
  });
}

/**
 * When user clicks "Enquire 1st Floor" or other floor buttons, pre-select that floor in the form
 */
function initFloorSelectTriggers() {
  document.querySelectorAll('[data-select-floor]').forEach(btn => {
    btn.addEventListener('click', function(e) {
      const targetFloor = this.getAttribute('data-select-floor');
      const floorSelect = document.getElementById('preferredFloor');
      if (floorSelect && targetFloor) {
        floorSelect.value = targetFloor;
      }
    });
  });
}

/**
 * Format and trigger direct WhatsApp conversation with owner
 */
function sendViaWhatsApp(form) {
  const name = form.querySelector('[name="tenant_name"]')?.value.trim() || 'Prospective Tenant';
  const phone = form.querySelector('[name="tenant_phone"]')?.value.trim() || 'Not specified';
  const tenantType = form.querySelector('[name="tenant_type"]')?.value || 'Family';
  const preferredFloor = form.querySelector('[name="preferred_floor"]')?.value || 'Any Available';
  const moveDate = form.querySelector('[name="move_in_date"]')?.value || 'Flexible';
  const notes = form.querySelector('[name="tenant_notes"]')?.value.trim() || 'Looking forward to scheduling a visit.';

  const message = 
`*Rental Enquiry - Hamid Residency*
---------------------------------------
*Name:* ${name}
*Phone:* ${phone}
*Profile:* ${tenantType}
*Preferred Floor:* ${preferredFloor}
*Target Move-in:* ${moveDate}
*Requirement / Timing:* ${notes}
---------------------------------------
(Sent via Hamid Residency Portal - Direct Owner Connection)`;

  const encodedMsg = encodeURIComponent(message);
  const whatsappUrl = `https://wa.me/${OWNER_CONFIG.phoneRaw}?text=${encodedMsg}`;

  // Open WhatsApp in new tab / app
  window.open(whatsappUrl, '_blank');
}

/**
 * Standard Form Submission fallback with friendly alert
 */
function handleFormSubmission(form) {
  const name = form.querySelector('[name="tenant_name"]')?.value.trim();
  const phone = form.querySelector('[name="tenant_phone"]')?.value.trim();

  if (!name || !phone) {
    alert('Please enter your Name and Mobile Number so the property owner can contact you.');
    return;
  }

  // Show inline success message
  const actionArea = form.querySelector('.form-actions');
  actionArea.innerHTML = `
    <div style="background: #e6f4ea; border: 1px solid #34a853; color: #137333; padding: 1.25rem; border-radius: 8px; text-align: center;">
      <h4 style="margin-bottom: 0.25rem; color: #137333;">Thank You, ${name}!</h4>
      <p style="font-size: 0.9rem; margin: 0;">Your enquiry details have been recorded. For fastest confirmation, you can message the landlord directly on WhatsApp.</p>
      <button type="button" class="btn btn-whatsapp btn-sm" style="margin-top: 0.75rem;" onclick="sendViaWhatsApp(document.getElementById('rentalEnquiryForm'))">
        Open in WhatsApp Now
      </button>
    </div>
  `;
}

/**
 * Visit Booking Modal
 */
function initVisitModal() {
  const modal = document.getElementById('visitModal');
  const triggerBtns = document.querySelectorAll('[data-open-visit-modal]');
  const closeBtn = document.getElementById('visitModalClose');

  if (!modal) return;

  triggerBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      modal.classList.add('open');
      document.body.style.overflow = 'hidden';
    });
  });

  const closeModal = () => {
    modal.classList.remove('open');
    document.body.style.overflow = '';
  };

  if (closeBtn) closeBtn.addEventListener('click', closeModal);

  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeModal();
  });
}
