// src/pages/Stats/Stats.js
import React from 'react';
import { useBook } from '../../context/BookContext';
import useBookStats from '../../hooks/useBookStats';
import './Stats.css';

const Stats = () => {
  const { books } = useBook();
  const stats = useBookStats(books);

  // Template literals untuk rendering dinamis
  const statCards = [
    { value: stats.total, label: 'Total Buku', description: `Total ${stats.total} buku dalam koleksi` },
    { value: stats.owned, label: 'Dimiliki', description: `${stats.owned} buku yang dimiliki` },
    { value: stats.reading, label: 'Sedang Dibaca', description: `${stats.reading} buku sedang dibaca` },
    { value: stats.wantToBuy, label: 'Ingin Dibeli', description: `${stats.wantToBuy} buku yang ingin dibeli` },
  ];

  return (
    <div className="stats-container">
      <h1>Statistik Buku</h1>
      <div className="stats-grid">
        {statCards.map((card, index) => {
          const cardTitle = `${card.value} ${card.label}`;
          const percentage = stats.total > 0 ? Math.round((card.value / stats.total) * 100) : 0;
          const percentageText = stats.total > 0 ? `(${percentage}%)` : '';
          
          return (
            <div key={index} className="stat-card" title={card.description}>
              <h2>{card.value}</h2>
              <p>{card.label} {percentageText && `- ${percentageText}`}</p>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default Stats;