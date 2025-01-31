function addTextBlock() {
    const editor = document.getElementById('editor');
    const textBlock = document.createElement('div');
    textBlock.className = 'text-block';
    textBlock.contentEditable = true;
    textBlock.innerText = 'Click here to edit text...';
    editor.appendChild(textBlock);
}

function addImageBlock() {
    const editor = document.getElementById('editor');
    const imageBlock = document.createElement('div');
    imageBlock.className = 'image-block';
    const image = document.createElement('img');
    image.src = 'https://via.placeholder.com/150';
    image.alt = 'Placeholder Image';
    imageBlock.appendChild(image);
    editor.appendChild(imageBlock);
}

function generateAIContent() {
    // Simulate AI-generated content
    const editor = document.getElementById('editor');
    const textBlock = document.createElement('div');
    textBlock.className = 'text-block';
    textBlock.contentEditable = true;
    textBlock.innerText = 'AI-generated content goes here...';
    editor.appendChild(textBlock);
}
