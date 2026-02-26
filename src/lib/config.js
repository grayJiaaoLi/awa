/**
 * @typedef {Object} Version
 * @property {string} id - The unique identifier for the version
 * @property {string} title - The display title of the version
 * @property {string} description - Brief description of what this version explores
 * @property {string} href - The URL path to the version
 * @property {string} [image] - Optional path to preview image
 */

/** @type {Version[]} */
export const versions = [
    {
        id: 'v1',
        title: 'Version 1',
        description: 'Initial simplified interface design.',
        href: '/v1',
        image: '/images/1.png'
    },
    {
        id: 'v2',
        title: 'Version 2',
        description: 'Advanced features with sidebar navigation.',
        href: '/v2',
        image: '/images/2.png'
    },
    {
        id: 'v3',
        title: 'Version 3',
        description: 'Experimental chat-centric layout.',
        href: '/v3',
        image: '/images/3.png'
    },
    {
        id: 'v4',
        title: 'Version 4',
        description: 'Minimalist distraction-free writing mode.',
        href: '/v4',
        image: '/images/4.png'
    }
];
